cd detector/
kubectl apply -f languages-51/isvc.yaml
kubectl apply -f lingua/isvc.yaml
kubectl apply -f xlm-roberta-base-language-detection/isvc.yaml
kubectl apply -f aggregate/isvc.yaml
cd ..
cd diffusers/v1
kubectl apply -f isvc.yaml
cd ../..
cd sentiment-analysis/
kubectl apply -f isvc.yaml
cd ..
cd translator
kubectl apply -f de-en/isvc.yaml
kubectl apply -f es-en/isvc.yaml
kubectl apply -f fr-en/isvc.yaml
kubectl apply -f ru-en/isvc.yaml
kubectl apply -f zh-en/isvc.yaml
cd ..
