fname = '../MS002 - Peptide de novo sequencing/peptidome validation/Wu_peptidome_p-mod_fdr5'
suffix = '_vs_human_all_isoform_v4'
peptide_loc = 9 ## column containing peptide sequence in the report

aa_list = 'GASPVTCLINDQKEMHFRYWmsty'
aa_mass_list = [57.02146,71.03711,87.03203,
                97.05276,99.06841,101.04768,
                103.00919 + 57.02146,113.08406,113.08406, ## C are C mod
                114.04293,115.02694,128.05858,
                128.09496,129.04259,131.04049,
                137.05891,147.06841,156.10111,
                163.06333,186.07931,131.04049 + 15.99491, ## m = M(ox)
                87.03203 + 79.96633,101.04768 + 79.96633,163.06333 + 79.96633] ## s = S(ph), t = T(ph), y = Y(ph)

proton = 1.007276

aa_mass = {}

for i in range(len(aa_list)):
    aa_mass[aa_list[i]] = aa_mass_list[i]

trivial_map = {}

for i in range(len(aa_list)):
    trivial_map['(' + str(aa_mass_list[i]) + ')'] = aa_list[i]

decode_map = {}

with open(fname + suffix + '.tsv', 'rt') as fin:
    for line in fin.readlines():
        content = line.rstrip('\n').split('\t')

        if not content[0] in decode_map:
            decode_map[content[0]] = {}

        if not content[5] in decode_map[content[0]]:
            decode_map[content[0]][content[5]] = []

        decode_map[content[0]][content[5]].append(content[3])

mod_seq_map = {}
base_seq_map = {}

for peptide in decode_map:
    candidates = set([x.upper() for x in decode_map[peptide]])

    if len(candidates) == 1:
        base_seq_map[peptide] = ', '.join(candidates)
        mod_seq_map[peptide] =', '.join(decode_map[peptide].keys())
    else:
        base_seq_map[peptide] = 'Ambiguous'
        mod_seq_map[peptide] = 'Ambiguous'

with open(fname + '.tsv', 'rt') as fin, open(fname + '_extended.tsv', 'w') as fout:
    header = fin.readline().strip()

    fout.write(header + '\tBaseSeq\tModSeq\n') # ProteinMapDetails\n')

    for line in fin.readlines():
        fout.write(line.strip())
        content = line.strip().split('\t')[peptide_loc]

        if not content in decode_map:
            for tag in trivial_map:
                content = content.replace(tag, trivial_map[tag])
            
            if not '(' in content: ## no mass tag
                if not 'I' in content: ## no I/L ambiguity
                    fout.write('\t' + content + '\t' + content + '\tUnMapped\n')
                else:
                    fout.write('\tAmbiguous\tAmbiguous\tUnMapped\n')
            else:
                fout.write('\tAmbiguous\tAmbiguous\tUnMapped\n')
        else:
            fout.write('\t' + base_seq_map[content] + '\t' + mod_seq_map[content] + '\n') # + str(decode_map[content]) + '\n')
