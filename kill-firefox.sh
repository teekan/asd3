#!/bin/bash
sudo kill $(pgrep firefox)
sudo find /tmp/ -name "rust_mozprofile*" -exec rm -r {} \;
sudo find /tmp/ -name "Temp-*" -exec rm -r {} \;
