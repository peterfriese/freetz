#!/bin/sh


. /usr/lib/libmodcgi.sh

check "$NETSNMP_ENABLED" yes:auto "*":man

sec_begin '$(lang de:"Starttyp" en:"Start type")'

cat << EOF
<p><input id="e1" type="radio" name="enabled" value="yes"$auto_chk><label
for="e1"> $(lang de:"Automatisch" en:"Automatic")</label><input id="e2" type="radio"
name="enabled" value="no"$man_chk><label for="e2"> $(lang de:"Manuell" en:"Manual")</label></p>
EOF

sec_end
sec_begin '$(lang de:"Konfiguration" en:"Configuration")'

cat << EOF
<ul>
<li><a href="$(href file netsnmp conf)">$(lang de:"snmpd.conf bearbeiten" en:"Edit snmpd.conf")</a></li>
</ul>
EOF

sec_end
