

#docker-compose exec bird17_1 bash -c "perl -pi -e 's/127.0.0.11/10.16.1.101/g' /etc/resolv.conf"

runtest ()
{
  POD=$1
  CMD=$2
  echo Running on pod $POD with command: $CMD
  docker-compose exec $POD $CMD
  echo
  echo
  sleep 2
}

# Clear screen
clear

runtest bird17_1 "curl http://10.16.2.101"
runtest bird17_1 "curl http://[fd00:16:2::101]"

runtest bird17_1 "host s1.p16001.lab 10.16.1.101"


for i in 16_1 16_2 17_1
do
  runtest bird$i "birdc show proto"
  runtest bird$i "birdc show route"
done

for i in 16_1 16_2 17_1
do
  runtest bird$i "birdc6 show proto"
  runtest bird$i "birdc6 show route"
done

#runtest bird17_1 "nmap --top-ports 10 -A -6 fd00:16:2::101"
