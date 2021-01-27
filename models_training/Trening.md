

# Trening

1. Do fine-tuningu wybraliśmy wielojęzyczny model o nazwie **paraphrase-xlm-r-multilingual-v1**, ponieważ uzyskał lepsze wyniki niż pozostałe wielojęzyczne modele podczas ewaluacji na naszych zbiorach testowych.

   Ewaluację przeprowadzaliśmy na dwa sposoby:

   1. **Sprawdzanie podobieństwa embeddingów** - Wykorzystując 1000 par zdań ze zbioru **CDSCorpus**, które w skali od 0 do 5 zostały ocenione pod względem podobieństwa, liczone były współczynniki korelacji Pearsona oraz Spearmana pomiędzy wartościami podobieństwa przewidzianymi przez model oraz wartościami oryginalnymi.
   2. **Wyszukiwanie informacji** - Wykorzystując 817 pytań i odpowiedzi ze zbioru **Czy wiesz?** dla każdego pytania wyszukiwane było 1, 3, 5 oraz 10 najbardziej podobnych odpowiedzi oraz za pomocą różnych metryk liczona była dokładność tego wyszukiwania, np. przy wykorzystaniu skuteczności.

   ### Sprawdzanie podobieństwa embeddingów

   | model | cosine_pearson                       | cosine_spearman | euclidean_pearson | euclidean_spearman | manhattan_pearson | manhattan_spearman | dot_pearson | dot_spearman |          |
   | ----- | ------------------------------------ | --------------- | ----------------- | ------------------ | ----------------- | ------------------ | ----------- | ------------ | -------- |
   | 0     | distiluse-base-multilingual-cased-v2 | 0.878515        | 0.877008          | 0.862547           | 0.876435          | 0.859509           | 0.873385    | 0.826851     | 0.829585 |
   | 1     | paraphrase-xlm-r-multilingual-v1     | 0.915836        | 0.910637          | 0.908304           | 0.907112          | 0.907047           | 0.905628    | 0.877705     | 0.865510 |
   | 2     | stsb-xlm-r-multilingual              | 0.887779        | 0.885161          | 0.875350           | 0.876960          | 0.874208           | 0.876437    | 0.838509     | 0.829004 |
   | 3     | quora-distilbert-multilingual        | 0.821687        | 0.849722          | 0.841780           | 0.842773          | 0.841113           | 0.842188    | 0.786613     | 0.785287 |

   ### Wyszukiwanie informacji (krótkie odpowiedzi)

   |      | model                                | Accuracy@1 | Accuracy@3 | Accuracy@5 | Accuracy@10 | Precision@1 | Recall@1 | Precision@3 | Recall@3 | Precision@5 | Recall@5 | Precision@10 | Recall@10 | MRR@10   | NDCG@10  | MAP@100  |
   | ---- | ------------------------------------ | ---------- | ---------- | ---------- | ----------- | ----------- | -------- | ----------- | -------- | ----------- | -------- | ------------ | --------- | -------- | -------- | -------- |
   | 0    | distiluse-base-multilingual-cased-v2 | 0.644800   | 0.770812   | 0.811709   | 0.858626    | 0.644800    | 0.644800 | 0.256937    | 0.770812 | 0.162342    | 0.811709 | 0.085863     | 0.858626  | 0.716071 | 0.750547 | 0.720487 |
   | 1    | paraphrase-xlm-r-multilingual-v1     | 0.836205   | 0.917584   | 0.937305   | 0.958896    | 0.836205    | 0.836205 | 0.305861    | 0.917584 | 0.187461    | 0.937305 | 0.095890     | 0.958896  | 0.880396 | 0.899635 | 0.881870 |
   | 2    | stsb-xlm-r-multilingual              | 0.590201   | 0.714137   | 0.756487   | 0.808595    | 0.590201    | 0.590201 | 0.238046    | 0.714137 | 0.151297    | 0.756487 | 0.080859     | 0.808595  | 0.662591 | 0.697816 | 0.667771 |
   | 3    | quora-distilbert-multilingual        | 0.602034   | 0.708532   | 0.747353   | 0.797177    | 0.602034    | 0.602034 | 0.236177    | 0.708532 | 0.149471    | 0.747353 | 0.079718     | 0.797177  | 0.665448 | 0.697121 | 0.670427 |

   ### Wyszukiwanie informacji (pasujące paragrafy)

   |      | model                                | Accuracy@1 | Accuracy@3 | Accuracy@5 | Accuracy@10 | Precision@1 | Recall@1 | Precision@3 | Recall@3 | Precision@5 | Recall@5 | Precision@10 | Recall@10 | MRR@10   | NDCG@10  | MAP@100  |
   | ---- | ------------------------------------ | ---------- | ---------- | ---------- | ----------- | ----------- | -------- | ----------- | -------- | ----------- | -------- | ------------ | --------- | -------- | -------- | -------- |
   | 0    | distiluse-base-multilingual-cased-v2 | 0.551381   | 0.678846   | 0.723895   | 0.779946    | 0.551381    | 0.551381 | 0.226282    | 0.678846 | 0.144779    | 0.723895 | 0.077995     | 0.779946  | 0.625284 | 0.662512 | 0.630700 |
   | 1    | paraphrase-xlm-r-multilingual-v1     | 0.605979   | 0.724725   | 0.763546   | 0.809633    | 0.605979    | 0.605979 | 0.241575    | 0.724725 | 0.152709    | 0.763546 | 0.080963     | 0.809633  | 0.674149 | 0.706916 | 0.678707 |
   | 2    | stsb-xlm-r-multilingual              | 0.405024   | 0.524393   | 0.582935   | 0.646253    | 0.405024    | 0.405024 | 0.174798    | 0.524393 | 0.116587    | 0.582935 | 0.064625     | 0.646253  | 0.479739 | 0.519575 | 0.487758 |
   | 3    | quora-distilbert-multilingual        | 0.461491   | 0.578368   | 0.628192   | 0.690471    | 0.461491    | 0.461491 | 0.192789    | 0.578368 | 0.125638    | 0.628192 | 0.069047     | 0.690471  | 0.533318 | 0.570937 | 0.540081 |

2. Trening na zbiorze CDSCorpus

   |      | epoch | steps | cosine_pearson | cosine_spearman | euclidean_pearson | euclidean_spearman | manhattan_pearson | manhattan_spearman | dot_pearson | dot_spearman |
   | ---- | ----- | ----- | -------------- | --------------- | ----------------- | ------------------ | ----------------- | ------------------ | ----------- | ------------ |
   | 0    | 0     | -1    | 0.945262       | 0.943640        | 0.925536          | 0.938948           | 0.924652          | 0.937446           | 0.932375    | 0.930739     |
   | 1    | 1     | -1    | 0.942300       | 0.938838        | 0.915326          | 0.932702           | 0.913458          | 0.930382           | 0.926201    | 0.925722     |
   | 2    | 2     | -1    | 0.945187       | 0.941700        | 0.919394          | 0.936077           | 0.917929          | 0.934123           | 0.932308    | 0.931346     |
   | 3    | 3     | -1    | 0.944985       | 0.941135        | 0.918172          | 0.935126           | 0.916880          | 0.933302           | 0.931915    | 0.930736     |
   | 4    | 4     | -1    | 0.945293       | 0.941413        | 0.918752          | 0.935038           | 0.917464          | 0.933323           | 0.932372    | 0.931269     |

   |      | epoch | steps | Accuracy@1 | Accuracy@3 | Accuracy@5 | Accuracy@10 | Precision@1 | Recall@1 | Precision@3 | Recall@3 | Precision@5 | Recall@5 | Precision@10 | Recall@10 | MRR@10  | NDCG@10  | MAP@100  |
   | ---- | ----- | ----- | ---------- | ---------- | ---------- | ----------- | ----------- | -------- | ----------- | -------- | ----------- | -------- | ------------ | --------- | ------- | -------- | -------- |
   | 0    | -1    | -1    | 0.935129   | 0.964504   | 0.977968   | 0.986536    | 0.935129    | 0.935129 | 0.321501    | 0.964504 | 0.195594    | 0.977968 | 0.098654     | 0.986536  | 0.95311 | 0.961268 | 0.953404 |

3. **Trening na zbiorze Czy wiesz?**

   |      | epoch | steps | cosine_pearson | cosine_spearman | euclidean_pearson | euclidean_spearman | manhattan_pearson | manhattan_spearman | dot_pearson | dot_spearman |
   | ---- | ----- | ----- | -------------- | --------------- | ----------------- | ------------------ | ----------------- | ------------------ | ----------- | ------------ |
   | 0    | 0     | -1    | 0.914551       | 0.920961        | 0.908521          | 0.920186           | 0.907404          | 0.918576           | 0.897446    | 0.900921     |
   | 1    | 1     | -1    | 0.917955       | 0.924192        | 0.914883          | 0.924385           | 0.913607          | 0.923270           | 0.896433    | 0.898905     |
   | 2    | 2     | -1    | 0.919206       | 0.925045        | 0.915071          | 0.925480           | 0.914059          | 0.924131           | 0.897722    | 0.900415     |
   | 3    | 3     | -1    | 0.918261       | 0.924286        | 0.915376          | 0.925457           | 0.914384          | 0.924303           | 0.893976    | 0.896490     |
   | 4    | 4     | -1    | 0.918040       | 0.924109        | 0.915388          | 0.925440           | 0.914428          | 0.924409           | 0.893350    | 0.895835     |

   |      | epoch | steps | Accuracy@1 | Accuracy@3 | Accuracy@5 | Accuracy@10 | Precision@1 | Recall@1 | Precision@3 | Recall@3 | Precision@5 | Recall@5 | Precision@10 | Recall@10 | MRR@10   | NDCG@10  | MAP@100  |
   | ---- | ----- | ----- | ---------- | ---------- | ---------- | ----------- | ----------- | -------- | ----------- | -------- | ----------- | -------- | ------------ | --------- | -------- | -------- | -------- |
   | 0    | -1    | -1    | 0.95104    | 0.974296   | 0.98164    | 0.985312    | 0.95104     | 0.95104  | 0.324765    | 0.974296 | 0.196328    | 0.98164  | 0.098531     | 0.985312  | 0.963547 | 0.968931 | 0.964054 |

4. **Trening najpierw na zbiorze CDSCorupus, potem na Czy wiesz?**

   |      | epoch | steps | cosine_pearson | cosine_spearman | euclidean_pearson | euclidean_spearman | manhattan_pearson | manhattan_spearman | dot_pearson | dot_spearman |
   | ---- | ----- | ----- | -------------- | --------------- | ----------------- | ------------------ | ----------------- | ------------------ | ----------- | ------------ |
   | 0    | 0     | -1    | 0.934637       | 0.934291        | 0.924644          | 0.935605           | 0.924642          | 0.934946           | 0.919902    | 0.918580     |
   | 1    | 1     | -1    | 0.934929       | 0.935999        | 0.926821          | 0.936227           | 0.927074          | 0.936264           | 0.919666    | 0.918646     |
   | 2    | 2     | -1    | 0.935879       | 0.936594        | 0.927955          | 0.937089           | 0.928309          | 0.936805           | 0.921432    | 0.919928     |
   | 3    | 3     | -1    | 0.935097       | 0.935786        | 0.927322          | 0.936316           | 0.927753          | 0.936106           | 0.920311    | 0.918692     |
   | 4    | 4     | -1    | 0.935031       | 0.935710        | 0.927321          | 0.936266           | 0.927759          | 0.936097           | 0.920194    | 0.918558     |

   |      | epoch | steps | Accuracy@1 | Accuracy@3 | Accuracy@5 | Accuracy@10 | Precision@1 | Recall@1 | Precision@3 | Recall@3 | Precision@5 | Recall@5 | Precision@10 | Recall@10 | MRR@10   | NDCG@10  | MAP@100  |
   | ---- | ----- | ----- | ---------- | ---------- | ---------- | ----------- | ----------- | -------- | ----------- | -------- | ----------- | -------- | ------------ | --------- | -------- | -------- | -------- |
   | 0    | -1    | -1    | 0.946144   | 0.974296   | 0.980416   | 0.985312    | 0.946144    | 0.946144 | 0.324765    | 0.974296 | 0.196083    | 0.980416 | 0.098531     | 0.985312  | 0.961201 | 0.967164 | 0.961576 |

5. **Trening najpierw na zbiorze Czy wiesz?, a potem na CDS**

   |      | epoch | steps | cosine_pearson | cosine_spearman | euclidean_pearson | euclidean_spearman | manhattan_pearson | manhattan_spearman | dot_pearson | dot_spearman |
   | ---- | ----- | ----- | -------------- | --------------- | ----------------- | ------------------ | ----------------- | ------------------ | ----------- | ------------ |
   | 0    | 0     | -1    | 0.941008       | 0.938770        | 0.919862          | 0.934821           | 0.918780          | 0.933031           | 0.924929    | 0.923331     |
   | 1    | 1     | -1    | 0.943041       | 0.940784        | 0.920623          | 0.937492           | 0.920431          | 0.936622           | 0.928853    | 0.927283     |
   | 2    | 2     | -1    | 0.943659       | 0.941161        | 0.919767          | 0.936890           | 0.918871          | 0.935027           | 0.930108    | 0.928762     |
   | 3    | 3     | -1    | 0.943084       | 0.940720        | 0.919439          | 0.936351           | 0.919036          | 0.935154           | 0.927629    | 0.926702     |
   | 4    | 4     | -1    | 0.943493       | 0.940801        | 0.920020          | 0.936554           | 0.919503          | 0.935140           | 0.928619    | 0.927225     |

   |      | epoch | steps | Accuracy@1 | Accuracy@3 | Accuracy@5 | Accuracy@10 | Precision@1 | Recall@1 | Precision@3 | Recall@3 | Precision@5 | Recall@5 | Precision@10 | Recall@10 | MRR@10   | NDCG@10  | MAP@100  |
   | ---- | ----- | ----- | ---------- | ---------- | ---------- | ----------- | ----------- | -------- | ----------- | -------- | ----------- | -------- | ------------ | --------- | -------- | -------- | -------- |
   | 0    | -1    | -1    | 0.932681   | 0.968176   | 0.976744   | 0.984088    | 0.932681    | 0.932681 | 0.322725    | 0.968176 | 0.195349    | 0.976744 | 0.098409     | 0.984088  | 0.952407 | 0.960227 | 0.952917 |

6. **Wytrenowanie Cross-Encodera na zbiorze CDSCorpus w celu zaetykietowania zbioru Czy wiesz? pod względem podobieństwa pytań i odpowiedzi, następnie wytrenowanie Bi-Encodera na zbiorze danych powstałym ze złączenia zbioru CDSCorpus oraz zaetykietowanego zbioru Czy wiesz?**

   W celu dotrenowania Cross-Encodera został użyty model **bert-base-multilingual-cased** z biblioteki HuggingFace, który nie był wcześniej trenowany specjalnie do produkowania jak najbardziej podobnych embeddingów dla podobnych znaczeniowo tekstów, lecz tylko na zadaniach typowych dla modelu BERT (MLM, Next Sentence Prediction).

   Różnica pomiędzy Bi-Encoderem a Cross-Encoderem polega na tym, że Bi-Encoder na wejściu przyjmuje zdania a następnie produkuje dla nich embeddingi, natomiast Cross-Encoder na wejściu przyjmuje pary zdań, a na wyjściu zwraca liczbę od 0 do 1 oznaczającą podobieństwo pomiędzy dwoma zdaniami.

   ![BiEncoder](https://raw.githubusercontent.com/UKPLab/sentence-transformers/master/docs/img/Bi_vs_Cross-Encoder.png)

   **Trening Cross-Encodera**

   |      | epoch | steps | Pearson_Correlation | Spearman_Correlation |
   | ---- | ----- | ----- | ------------------- | -------------------- |
   | 0    | 0     | -1    | 0.951461            | 0.946899             |
   | 1    | 1     | -1    | 0.955849            | 0.948760             |
   | 2    | 2     | -1    | 0.955449            | 0.948027             |
   | 3    | 3     | -1    | 0.957139            | 0.950373             |
   | 4    | 4     | -1    | 0.959788            | 0.951573             |
   | 5    | 5     | -1    | 0.958071            | 0.949099             |
   | 6    | 6     | -1    | 0.957797            | 0.948580             |
   | 7    | 7     | -1    | 0.957270            | 0.948293             |
   | 8    | 8     | -1    | 0.957591            | 0.948188             |
   | 9    | 9     | -1    | 0.957573            | 0.948150             |

   **Trening Bi-Encodera**

   |      | epoch | steps | cosine_pearson | cosine_spearman | euclidean_pearson | euclidean_spearman | manhattan_pearson | manhattan_spearman | dot_pearson | dot_spearman |
   | ---- | ----- | ----- | -------------- | --------------- | ----------------- | ------------------ | ----------------- | ------------------ | ----------- | ------------ |
   | 0    | 0     | -1    | 0.939529       | 0.938488        | 0.922024          | 0.932723           | 0.921453          | 0.931622           | 0.925220    | 0.924558     |
   | 1    | 1     | -1    | 0.943479       | 0.940721        | 0.922770          | 0.935424           | 0.921906          | 0.934204           | 0.925533    | 0.924305     |
   | 2    | 2     | -1    | 0.943445       | 0.940915        | 0.919063          | 0.933215           | 0.918023          | 0.931593           | 0.929880    | 0.928767     |
   | 3    | 3     | -1    | 0.944208       | 0.941721        | 0.919334          | 0.934654           | 0.918480          | 0.933238           | 0.929471    | 0.928849     |
   | 4    | 4     | -1    | 0.944674       | 0.942114        | 0.919317          | 0.934806           | 0.918335          | 0.933238           | 0.929866    | 0.929383     |

   |      | epoch | steps | Accuracy@1 | Accuracy@3 | Accuracy@5 | Accuracy@10 | Precision@1 | Recall@1 | Precision@3 | Recall@3 | Precision@5 | Recall@5 | Precision@10 | Recall@10 | MRR@10   | NDCG@10 | MAP@100  |
   | ---- | ----- | ----- | ---------- | ---------- | ---------- | ----------- | ----------- | -------- | ----------- | -------- | ----------- | -------- | ------------ | --------- | -------- | ------- | -------- |
   | 0    | -1    | -1    | 0.820073   | 0.877601   | 0.893513   | 0.916769    | 0.820073    | 0.820073 | 0.292534    | 0.877601 | 0.178703    | 0.893513 | 0.091677     | 0.916769  | 0.852552 | 0.86812 | 0.854271 |

