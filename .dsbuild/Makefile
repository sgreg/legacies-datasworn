DATASWORN_ID = legacies
VERSION ?= $(shell /bin/date +%Y%m%d-%H%M%S)
OUTDIR ?= dist
OUTFILE = $(OUTDIR)/$(DATASWORN_ID)-datasworn-$(VERSION).json

all: get

sanity:
	@if [[ ${PWD}/ == */.dsbuild/ || ! -d .dsbuild ]] ; then\
		echo "Must be run from source repository root directory";\
		echo "";\
		exit 1;\
	fi
	@mkdir -p ${OUTDIR}

build: sanity
	docker rm -i dsbuilder
	docker run --name dsbuilder --volume .:/data:z datasworn-builder:0.1 /data/.dsbuild

get: build
	docker cp dsbuilder:/home/datasworn/datasworn/datasworn/$(DATASWORN_ID)/$(DATASWORN_ID).json $(OUTFILE)
	@echo ""
	@ls -l $(OUTFILE)

