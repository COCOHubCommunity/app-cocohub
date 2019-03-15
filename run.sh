for f in `cat languages`
do
    bash project.sh "$f"
    if [ $? -ne 0]
    then
        break
    fi
done
