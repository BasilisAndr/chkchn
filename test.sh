#!/bin/bash
echo "positive test"
hfst-pair-test -i popytka.hfst -I test.test
echo "negative test"
hfst-pair-test -N -i popytka.hfst -I neg.test.test
