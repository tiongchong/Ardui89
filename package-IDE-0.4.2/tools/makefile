# Fichier cible
TARGET=package_ardui89_index.json
SDCC_VERSION=4.4.0
FAKECC_VERSION=0.2.5
#STCFLASHISP_VERSION=0.2.1
PYTHON_STCGAL_VERSION=0.3
HOST = x86_64-apple-darwin
# Liste des fichiers source
#DSRCS = sdcc-$(SDCC_VERSION)-$(HOST) fake_cc-$(FAKECC_VERSION)-$(HOST) stcflashisp-$(STCFLASHISP_VERSION)-$(HOST)
DSRCS = sdcc-$(SDCC_VERSION)-$(HOST) fake_cc-$(FAKECC_VERSION)-$(HOST) python3-3.8-stcgal-$(PYTHON_STCGAL_VERSION)-$(HOST)
# Liste des fichiers objets
TGZ = $(DSRCS:=.tar.gz)
MKTOOL = $(DSRCS:=.json)
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

mingw32:
	make -f makefile_i686-mingw32.sub

linux:
	make -f makefile_i686-pc-linux-gnu.sub
