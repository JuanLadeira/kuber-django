1. Test django project
'''
python manage.py test
'''
2. build container
'''
EXAMPLE: docker build -f Dockerfile \ 
                -t registry.gitialocean.com/<container-registry-name>/<image-name>:<tag> 
REAL:
    docker build -f Dockerfile \ 
    -t registry.digitalocean.com/k8s-django/django-k8s-web:latest \
    -t registry.digitalocean.com/k8s-django/django-k8s-web:v1 \
    .

'''
3. Push this container to de digitalocean container registry
'''
docker push  registry.digitalocean.com/k8s-django/django-k8s-web --all-tags
'''
4. update secrets
'''
kubectl delete secret django-k8s-web-prod-env
kubectl create secret generic django-k8s-web-prod-env --from-env-file=web/env.prod
'''
5. Update Deployment

'''
kubectl apply -f k8s/apps/django-k8s-web.yaml 
'''

6. Wait to rollout to finish
'''
kubectl rollout status deployment django-k8s-web-deployment
'''

7. Migrate Database
'''
export SINGLE_POD_NAME=S(kubectl get pod -l app=django-k8s-web-deployment -o jsonpath="{.items[0].metadata.name}")
'''
or
'''
export SINGLE_POD_NAME=S(kubectl get pod -l app=django-k8s-web-deployment -o NAME | tail -n 1)
'''
8. run the migrations
'''
kubectl exec -it $SINGLE_POD_NAME -- sh /app/migrate.sh

