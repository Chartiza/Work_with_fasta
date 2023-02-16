with open('Needed_contigs_list.txt') as f:
    contigs = f.read().splitlines()

with open('Output_contigs.fasta','w') as f:
  for l in open('Input_contigs.fasta'):
    if '>' in l:
      data=l.rstrip().split(' ')
      contig_name = data[0][1:]
      if contig_name in contigs:
        print(contig_name)
        f.write(l)
        flag=1
      else:
        flag=0
    else:
      if flag==1:
        f.write(l)
