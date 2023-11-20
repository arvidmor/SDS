#/env/bin bash
echo "How many words?"
read input

pass=$(shuf -n $input /usr/share/dict/words)
echo $pass

noWords=$(wc /usr/share/dict/words | cut -d " " -f 5)
echo "$input random words form a word list of $noWords words"

keyspace=26

if [[ $pass=~[[:upper:]] ]]
then
    keyspace+=26
fi

if [[ $pass==[[*['!'@#\$%^\&_+\']*]] ]]
then
    keyspace+=13
fi
echo $keyspace
# echo "Entropy: "