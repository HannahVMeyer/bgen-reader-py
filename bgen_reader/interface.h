typedef char byte;
typedef int_fast64_t inti;
typedef double real;

typedef struct string {
    inti len;
    byte* str;
} string;

struct BGenVar {
    string id;
    string rsid;
    string chrom;
    inti position;
    inti nalleles;
    string* allele_ids;
};

struct BGenVI;
struct BGenVG;

struct BGenFile* open_bgen(const byte* filepath);

void close_bgen(struct BGenFile* bgen);

inti get_nsamples(struct BGenFile* bgen);

inti get_nvariants(struct BGenFile* bgen);

string* read_samples(struct BGenFile* bgen);

void free_samples(const struct BGenFile* bgen,
    string* samples);

struct BGenVar* read_variants(struct BGenFile* bgen,
    struct BGenVI** index);

inti store_variants(const struct BGenFile*, struct BGenVar*, struct BGenVI*,
    const byte*);

struct BGenVar* load_variants(struct BGenFile* bgen,
    const byte* cache_filepath,
    struct BGenVI** index);

void free_variants(const struct BGenFile* bgen,
    struct BGenVar* variants);

void free_index(struct BGenVI* index);

struct BGenVG* open_variant_genotype(struct BGenVI* index,
    inti variant_idx);

void read_variant_genotype(struct BGenVI* index,
    struct BGenVG* vg,
    real* probabilities);

inti get_nalleles(struct BGenVG* vg);
inti get_ploidy(struct BGenVG* vg);
inti get_ncombs(struct BGenVG* vg);

void close_variant_genotype(struct BGenVI* index,
    struct BGenVG* vg);

void free(void*);

string string_duplicate(const string s);

inti sample_ids_presence(struct BGenFile* bgen);
