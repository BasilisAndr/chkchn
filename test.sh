#!/bin/bash
echo "positive test"
hfst-pair-test -i ckt.twol.hfst -I test.test
echo "negative test"
hfst-pair-test -N -i ckt.twol.hfst -I neg.test.test
