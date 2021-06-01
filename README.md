# MapReduce-on-Hadoop-HDFS
Preparing your Hadoop infrastructure. Implementing WordCount MapReduce on Hadoop HDFS

In order to practically understand how data flows through a map and reduce computational pipeline,
you are going to implement a WordCount example yourself. WordCount is a simple application that
counts the number of occurrences of each word in a given input set. We have already implemented this
program as part of our very first lab, you can reuse your data cleaning methods from the first lab, you
can also use external libraries here for data cleaning (removing punctuations, links, etc.) and stop word
removal, you should be left with only the useful words before you start counting them. Hadoop streaming
serializes data on a line-by-line basis, all python programs have to be adapted to it the streaming nature
of Hadoop. This can be done simply by reading inputs from stdin and writing outputs to stdout. This
is different from what we have encountered in the previous labs where we read inputs from files stored
on our local filesystems and writing outputs to our stdout.
