#!/bin/bash
for i in {1..100}
do
  mkdir ./$i
  for j in {1..1000}
  do
    touch ./$i/file_$j.txt
  done
done
