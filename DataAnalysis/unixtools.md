* Count the number of columns
awk -F',' '{print NF; exit}' filename
 * F is field separator
 * NF is inbuilt variable, gives the number of fields

* Append a column to a csv file
awk -F, '{$(NF+1)="someval";}1' OFS=, input.txt > output.txt
