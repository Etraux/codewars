#!/bin/bash

# your code here #input text as $1,output as result

echo $1 | sed 's/[aeiouAEIOU]//g'