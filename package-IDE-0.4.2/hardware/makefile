# Fichier cible
TARGET=package_ardui89_index.json
VERSION=0.4.2
# Liste des fichiers source
DSRCS = ardui89-$(VERSION)
# Liste des fichiers objets
TGZ = $(DSRCS:=.tar.gz)
MKTOOL = $(DSRCS:=.json)
HOST = x86_64-apple-darwin
URL = https://master.dl.sourceforge.net/project/stc89/packages/
# Règle par défaut : construire l'exécutable
all: clear_MAC_METADATA $(TARGET)
# Règle pour construire l'exécutable
$(TARGET): $(TGZ) $(MKTOOL)
	echo "Done. Ready for : $(TARGET)"
# Règle pour construire les fichiers objets
%.tar.gz: %
	COPYFILE_DISABLE=1 tar --exclude='.DS_Store' --exclude='._*' --exclude='__MACOSX' -cvzf $@ $<
%.json: %
	./mktooljson/mktooljson $<.tar.gz $(HOST) $(URL)$<.tar.gz
# Règle pour nettoyer les fichiers de construction
clean:
	rm -f $(TGZ)
.PHONY: all clean clear_MAC_METADATA

clear_MAC_METADATA:
	find . -name ".DS_Store" -type f -delete
	find . -name "._*" -type f -delete
