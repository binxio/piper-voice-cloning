alias modelay='f() { docker run -e INPUT_STRING="$1" -v $(pwd):/output containername && open ./output.wav; unset -f f; }; f'
