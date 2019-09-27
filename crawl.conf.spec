#   Version 6.6.2
#
# This file contains possible attribute/value pairs for configuring crawl.
#
# There is a crawl.conf in $SPLUNK_HOME/etc/system/default/.  To set custom
# configurations, place a crawl.conf in $SPLUNK_HOME/etc/system/local/. For
# help, see crawl.conf.example. You must restart Splunk to enable
# configurations.
#
# To learn more about configuration files (including precedence) please see the
# documentation located at
# http://docs.splunk.com/Documentation/Splunk/latest/Admin/Aboutconfigurationfiles
#
# Set of attribute-values used by crawl.
#
# If attribute, ends in _list, the form is:
#
#      attr = val, val, val, etc.
#
# The space after the comma is necessary, so that "," can be used, as in
# BAD_FILE_PATTERNS's use of "*,v"

# GLOBAL SETTINGS
# Use the [default] stanza to define any global settings.
#   * You can also define global settings outside of any stanza, at the top of
#     the file.
#   * Each conf file should have at most one default stanza. If there are
#     multiple default stanzas, attributes are combined. In the case of
#     multiple definitions of the same attribute, the last definition in the
#     file wins.
#   * If an attribute is defined at both the global level and in a specific
#     stanza, the value in the specific stanza takes precedence.


[default]

[files]
* Sets file crawler-specific attributes under this stanza header.
* Follow this stanza name with any of the following attributes.

root = <semi-colon separate list of directories>
* Set a list of directories this crawler should search through.
* Defaults to /;/Library/Logs

bad_directories_list = <comma-separated list of bad directories>
* List any directories you don't want to crawl.
* Defaults to:
        bin, sbin, boot, mnt, proc, tmp, temp, dev, initrd, help, driver, drivers, share, bak, old, lib, include, doc, docs, man, html, images, tests, js, dtd, org, com, net, class, java, resource, locale, static, testing, src, sys, icons, css, dist, cache, users, system, resources, examples, gdm, manual, spool, lock, kerberos, .thumbnails, libs, old, manuals, splunk, splunkpreview, mail, resources, documentation, applications, library, network, automount, mount, cores, lost\+found, fonts, extensions, components, printers, caches, findlogs, music, volumes, libexec

bad_extensions_list = <comma-separated list of file extensions to skip>
* List any file extensions and crawl will skip files that end in those extensions.
* Defaults to:
        0t, a, adb, ads, ali, am, asa, asm, asp, au, bak, bas, bat, bmp, c, cache, cc, cg, cgi, class, clp, com, conf, config, cpp, cs, css, csv, cxx, dat, doc, dot, dvi, dylib, ec, elc, eps, exe, f, f77, f90, for, ftn, gif, h, hh, hlp, hpp, hqx, hs, htm, html, hxx, icns, ico, ics, in, inc, jar, java, jin, jpeg, jpg, js, jsp, kml, la, lai, lhs, lib, license, lo, m, m4, mcp, mid, mp3, mpg, msf, nib, nsmap, o, obj, odt, ogg, old, ook, opt, os, os2, pal, pbm, pdf, pdf, pem, pgm, php, php3, php4, pl, plex, plist, plo, plx, pm, png, po, pod, ppd, ppm, ppt, prc, presets, ps, psd, psym, py, pyc, pyd, pyw, rast, rb, rc, rde, rdf, rdr, res, rgb, ro, rsrc, s, sgml, sh, shtml, so, soap, sql, ss, stg, strings, tcl, tdt, template, tif, tiff, tk, uue, v, vhd, wsdl, xbm, xlb, xls, xlw, xml, xsd, xsl, xslt, jame, d, ac, properties, pid, del, lock, md5, rpm, pp, deb, iso, vim, lng, list

bad_file_matches_list = <comma-separated list of regex>
* Crawl applies the specified regex and skips files that match the patterns.
* There is an implied "$" (end of file name) after each pattern.
* Defaults to:
        *~, *#, *,v, *readme*, *install, (/|^).*, *passwd*, *example*, *makefile, core.*

packed_extensions_list = <comma-separated list of extensions>
* Specify extensions of compressed files to exclude.
* Defaults to:
        bz, bz2, tbz, tbz2, Z, gz, tgz, tar, zip

collapse_threshold = <integer>
* Specify the minimum number of files a source must have to be considered a
  directory.
* Defaults to 1000.

days_sizek_pairs_list = <comma-separated hyphenated pairs of integers>
* Specify a comma-separated list of age (days) and size (kb) pairs to constrain
  what files are crawled.
* For example: days_sizek_pairs_list = 7-0, 30-1000 tells Splunk to crawl only
  files last modified within 7 days and at least 0kb in size, or modified
  within the last 30 days and at least 1000kb in size.
* Defaults to 30-0.

big_dir_filecount = <integer>
* Skip directories with files above <integer>
* Defaults to 10000.

index = <$INDEX>
* Specify index to add crawled files to.
* Defaults to main.

max_badfiles_per_dir = <integer>
* Specify how far to crawl into a directory for files.
* Crawl excludes a directory if it doesn't find valid files within the
  specified max_badfiles_per_dir.
* Defaults to 100.




[network]
* Sets network crawler-specific attributes under this stanza header.
* Follow this stanza name with any of the following attributes.

host = <host or ip>
* default host to use as a starting point for crawling a network
* Defaults to 'localhost'.

subnet = <int>
* default number of bits to use in the subnet mask. Given a host with IP
  123.123.123.123, a subnet value of 32, would scan only that host, and a value
  or 24 would scan 123.123.123.*.
* Defaults to 32.
