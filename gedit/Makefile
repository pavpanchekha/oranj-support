PREFIX=/usr

install: oranj.xml
	cp oranj.xml ${PREFIX}/share/gtksourceview-2.0/language-specs/oranj.lang
	chmod a+r ${PREFIX}/share/gtksourceview-2.0/language-specs/oranj.lang
	update-mime-database ${PREFIX}/share/mime/
	# Fix to actually determine right directory
