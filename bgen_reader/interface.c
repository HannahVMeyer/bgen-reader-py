#include <stdio.h>
#include <stdlib.h>

#include "bgen.h"

struct BGenVI;
struct BGenVG;

struct BGenFile *open_bgen(const char *filepath) {
  return bgen_open(filepath);
}

void close_bgen(struct BGenFile *bgen) { bgen_close(bgen); }

int get_nsamples(struct BGenFile *bgen) { return bgen_nsamples(bgen); }

int get_nvariants(struct BGenFile *bgen) { return bgen_nvariants(bgen); }

string *read_samples(struct BGenFile *bgen, int verbose) { return bgen_read_samples(bgen, verbose); }

void free_samples(const struct BGenFile *bgen, string *samples) {
  bgen_free_samples(bgen, samples);
}

int store_variants(const struct BGenFile *bgen, struct BGenVar *v,
                   struct BGenVI *i, const char *fp) {
  return bgen_store_variants(bgen, v, i, fp);
}

struct BGenVar *load_variants(struct BGenFile *bgen, const char *cache_filepath,
                              struct BGenVI **index, int verbose) {
  return bgen_load_variants(bgen, cache_filepath, index, verbose);
}

struct BGenVar *read_variants(struct BGenFile *bgen, struct BGenVI **index, int verbose) {
  return bgen_read_variants(bgen, index, verbose);
}

void free_variants(const struct BGenFile *bgen, struct BGenVar *variants) {
  bgen_free_variants(bgen, variants);
}

void free_index(struct BGenVI *index) { bgen_free_index(index); }

struct BGenVG *open_variant_genotype(struct BGenVI *index, int variant_idx) {
  return bgen_open_variant_genotype(index, variant_idx);
}

void read_variant_genotype(struct BGenVI *index, struct BGenVG *vg,
                           double *probabilities) {
  bgen_read_variant_genotype(index, vg, probabilities);
}

int get_nalleles(struct BGenVG *vg) { return bgen_nalleles(vg); }

int get_ploidy(struct BGenVG *vg) { return bgen_ploidy(vg); }

int get_ncombs(struct BGenVG *vg) { return bgen_ncombs(vg); }

void close_variant_genotype(struct BGenVI *index, struct BGenVG *vg) {
  bgen_close_variant_genotype(index, vg);
}

string string_duplicate(string s) {
  string r;

  r.str = malloc(s.len);
  memcpy(r.str, s.str, s.len);
  r.len = s.len;
  return r;
}

int sample_ids_presence(struct BGenFile *bgen) {
  return bgen_sample_ids_presence(bgen);
}
