# define bins set
bin_name = set()

for l in open('MAIN_results_BinContis.csv'):
    data=l.rstrip().split(',')
    if data[0][1:] != 'init_bin_name':
        if data[0][1:] not in bin_name:
            bin_name.add(data[0])

for bin in bin_name:
    print(bin)

    # define contigs belongs to particular bin
    contigs = set()
    for l in open('MAIN_results_BinContis.csv'):
        data=l.rstrip().split(',')
        if data[7] != 'Final_bin_name':
            if data[7] == bin:
                contigs.add(data[1])

    # write out new contigs set for each bins
    with open('new_'+bin+'.fa','w') as f:
        for l in open('all_binned_contigs.fa'):
            if '>' in l:
                data=l.rstrip().split(' ')
                contig_name = data[0][1:]
                if contig_name in contigs:
                    #print(contig_name)
                    f.write(l)
                    flag=1
                else:
                    flag=0
            else:
                if flag==1:
                    f.write(l)
