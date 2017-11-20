#include <stdio.h>
#include <stdlib.h>

#include "bgen/bgen.h"

struct BGenVI;
struct BGenVG;

struct BGenFile* open_bgen(const byte* filepath)
{
    return bgen_open(filepath);
}

void close_bgen(struct BGenFile* bgen)
{
    bgen_close(bgen);
}

inti get_nsamples(struct BGenFile* bgen)
{
    return bgen_nsamples(bgen);
}

inti get_nvariants(struct BGenFile* bgen)
{
    return bgen_nvariants(bgen);
}

string* read_samples(struct BGenFile* bgen)
{
    return bgen_read_samples(bgen);
}

void free_samples(const struct BGenFile* bgen,
    string* samples)
{
    bgen_free_samples(bgen, samples);
}

inti store_variants(const struct BGenFile* bgen, struct BGenVar* v,
    struct BGenVI* i, const byte* fp)
{
    return bgen_store_variants(bgen, v, i, fp);
}

struct BGenVar* load_variants(struct BGenFile* bgen,
    const byte* cache_filepath,
    struct BGenVI** index)
{
    return bgen_load_variants(bgen, cache_filepath, index);
}

struct BGenVar* read_variants(struct BGenFile* bgen,
    struct BGenVI** index)
{
    return bgen_read_variants(bgen, index);
}

void free_variants(const struct BGenFile* bgen,
    struct BGenVar* variants)
{
    bgen_free_variants(bgen, variants);
}

void free_index(struct BGenVI* index)
{
    bgen_free_index(index);
}

struct BGenVG* open_variant_genotype(struct BGenVI* index,
    inti variant_idx)
{
    return bgen_open_variant_genotype(index, variant_idx);
}

void read_variant_genotype(struct BGenVI* index,
    struct BGenVG* vg,
    real* probabilities)
{
    bgen_read_variant_genotype(index, vg, probabilities);
}

inti get_nalleles(struct BGenVG* vg)
{
    return bgen_nalleles(vg);
}

inti get_ploidy(struct BGenVG* vg)
{
    return bgen_ploidy(vg);
}

inti get_ncombs(struct BGenVG* vg)
{
    return bgen_ncombs(vg);
}

void close_variant_genotype(struct BGenVI* index,
    struct BGenVG* vg)
{
    bgen_close_variant_genotype(index, vg);
}

string string_duplicate(string s)
{
    string r;

    r.str = malloc(s.len);
    memcpy(r.str, s.str, s.len);
    r.len = s.len;
    return r;
}

inti sample_ids_presence(struct BGenFile* bgen)
{
    return bgen_sample_ids_presence(bgen);
}
