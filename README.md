# deploy_selenium_grid_in_kubes

in gcp :

## create a cluster
1. create kubernetes cluster * 3 nodes
## install selenium hub 
2. kubectl apply -f  selenium-hub-rc.yml 
## install selenium hub as a nodeport service
3. kubectl apply -f  selenium-hub-service.yml
## expose service to do loadbalance and get a external ip
4. kubectl expose rc selenium-hub --name=selenium-hub-external --labels="app=selenium-hub,external=true" --type="LoadBalancer"
## chrome webdriver
5. kubectl apply -f  selenium-agent-rc.yml 
## chrome test enviroment
6. kubectl run selenium-python --image=google/python-hello 
## get pod id
7. export PODNAME=`kubectl get pods --selector="run=selenium-python" --output=template --template="{{with index .items 0}}{{.metadata.name}}{{end}}"`
## install selenium python package 
8. kubectl exec --stdin=true --tty=true $PODNAME -- pip install selenium
## run test case
9. kubectl exec --stdin=true --tty=true $PODNAME -- python test2.py --driverip=${driverip} --testurl=http://${testurl}/test.php

example:
$ ~/git_project$ kubectl get service
NAME                    TYPE           CLUSTER-IP      EXTERNAL-IP      PORT(S)          AGE
kubernetes              ClusterIP      10.15.240.1     <none>           443/TCP          1d
selenium-hub            NodePort       10.15.243.207   <none>           4444:30718/TCP   1d
selenium-hub-external   LoadBalancer   10.15.243.69    35.229.159.251   4444:30566/TCP   1d

$ ~/git_project$ kubectl get pods
NAME                               READY     STATUS    RESTARTS   AGE
selenium-hub-qnmbw                 1/1       Running   0          1d
selenium-node-chrome-b79p8         1/1       Running   0          1d
selenium-node-chrome-g8f8c         1/1       Running   0          1d
selenium-node-chrome-gjhst         1/1       Running   0          1d
selenium-node-chrome-lh742         1/1       Running   0          1d
selenium-node-chrome-p4gsk         1/1       Running   0          1d
selenium-node-chrome-vd867         1/1       Running   0          1d
selenium-node-chrome-wbnx4         1/1       Running   0          1d
selenium-python-6479976d89-4wmqj   1/1       Running   0          1d
$ kubectl get nodes
NAME                                       STATUS    ROLES     AGE       VERSION
gke-cluster-2-default-pool-f8543da3-7mq6   Ready     <none>    1d        v1.8.8-gke.0
gke-cluster-2-default-pool-f8543da3-q9t4   Ready     <none>    1d        v1.8.8-gke.0
gke-cluster-2-default-pool-f8543da3-xzjh   Ready     <none>    1d        v1.8.8-gke.0
  
## update service
kubectl replace --force  -f selenium-node-chrome-rc.yaml
## expand selenium grid
kubectl scale rc selenium-node-chrome --replicas=7
