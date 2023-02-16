with open('C:/path/Bal_1_mams.txt') as f:
    contigs = f.read().splitlines()

with open('12_contigs.fasta','w') as f:
  for l in open('canu_subreads.unassembled.fasta'):
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
