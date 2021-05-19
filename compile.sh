#!/bin/sh
protoc -I=. --python_out=. collectionset.proto 
