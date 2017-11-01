import sys
import ldap
from ldap.controls import SimplePagedResultsControl


LDAPSERVER='ldap://ldap.yourcompany.com:389'
BASEDN='dc=test,dc=com'
LDAPUSER = 'test'
LDAPPASSWORD = 'password'
PAGESIZE = 10
#ATTRLIST = ['uid', 'shadowLastChange', 'shadowMax', 'shadowExpire']

SEARCHFILTER='(CN=Test*)'


def create_controls(pagesize):
    """Create an LDAP control with a page size of "pagesize"."""
    # Initialize the LDAP controls for paging. Note that we pass ''
    # for the cookie because on first iteration, it starts out empty.
    return SimplePagedResultsControl(True, size=pagesize, cookie='')


def get_pctrls(serverctrls):
    """Lookup an LDAP paged control object from the returned controls."""
    # Look through the returned controls and find the page controls.
    # This will also have our returned cookie which we need to make
    # the next search request.
    return [c for c in serverctrls if c.controlType == SimplePagedResultsControl.controlType]

def set_cookie(lc_object, pctrls, pagesize):
    """Push latest cookie back into the page control."""
    cookie = pctrls[0].cookie
    lc_object.cookie = cookie
    return cookie

# This is essentially a placeholder callback function. You would do your real
# work inside of this. Really this should be all abstracted into a generator...
def process_entry(dn, attrs):
    """Process an entry. The two arguments passed are the DN and
       a dictionary of attributes."""
    print dn, attrs

# Ignore server side certificate errors (assumes using LDAPS and
# self-signed cert). Not necessary if not LDAPS or it's signed by
# a real CA.
ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_ALLOW)
# Don't follow referrals
ldap.set_option(ldap.OPT_REFERRALS, 0)

l = ldap.initialize(LDAPSERVER)
l.protocol_version = 3          # Paged results only apply to LDAP v3
try:
    l.simple_bind_s(LDAPUSER, LDAPPASSWORD)
except ldap.LDAPError as e:
    exit('LDAP bind failed: %s' % e)


msgid = l.search_s(BASEDN, ldap.SCOPE_BASE, SEARCHFILTER)
print len(msgid)

msgid = l.search_s(BASEDN, ldap.SCOPE_ONELEVEL, SEARCHFILTER)
print len(msgid)

#check how many items
msgid = l.search_s(BASEDN, ldap.SCOPE_SUBTREE, SEARCHFILTER)
print len(msgid)

# Create the page control to work from
lc = create_controls(PAGESIZE)

# Do searches until we run out of "pages" to get from
# the LDAP server.
while True:
    # Send search request
    try:
        # If you leave out the ATTRLIST it'll return all attributes
        # which you have permissions to access. You may want to adjust
        # the scope level as well (perhaps "ldap.SCOPE_SUBTREE", but
        # it can reduce performance if you don't need it).

        msgid = l.search_ext(BASEDN, ldap.SCOPE_SUBTREE, SEARCHFILTER, serverctrls=[lc])
        print msgid

    except ldap.LDAPError as e:
        sys.exit('LDAP search failed: %s' % e)


    # Pull the results from the search request
    try:
        rtype, rdata, rmsgid, serverctrls = l.result3(msgid)
        for i in rdata:
            print i[0]
    except ldap.LDAPError as e:
        sys.exit('Could not pull LDAP results: %s' % e)

    # Each "rdata" is a tuple of the form (dn, attrs), where dn is
    # a string containing the DN (distinguished name) of the entry,
    # and attrs is a dictionary containing the attributes associated
    # with the entry. The keys of attrs are strings, and the associated
    # values are lists of strings.
    # for dn, attrs in rdata:
    #     process_entry(dn, attrs)

    # Get cookie for next request
    pctrls = get_pctrls(serverctrls)
    if not pctrls:
        print >> sys.stderr, 'Warning: Server ignores RFC 2696 control.'
        break

    # Ok, we did find the page control, yank the cookie from it and
    # insert it into the control for our next search. If however there
    # is no cookie, we are done!
    cookie = set_cookie(lc, pctrls, PAGESIZE)
    if not cookie:
        break

# Clean up
l.unbind()

# Done!
sys.exit(0)
