# Example code that we include into a LaTeX-document
for FILE in *.dat
do
  wc -l ${FILE} | sort -g -n
done
