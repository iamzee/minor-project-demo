data = [
    'A great game',
    'The Election is over',
    'Very clean match',
    'A clean and unforgettable match',
    'It was a close elction'
]

targets = [0, 1, 0, 0, 1]

# CALCULATING PROBABILITY OF EACH CLASS ====================================
pi = dict()
for i in range(len(targets)):
    if targets[i] not in pi:
        pi[targets[i]] = 1
    else:
        pi[targets[i]] += 1


for key, value in pi.items():
    pi[key] = pi[key] / len(targets)

print("PROBABILITY OF EACH CLASS ==============================")
print(pi)


# FEATURE EXTACTION ==============================================
def feature_extraction(data):

    # BUILDING VOCABULARY
    vocabulary = dict()
    count = 0
    for i in range(len(data)):
        article = data[i].split()
        for j in range(len(article)):
            article[j] = article[j].capitalize()
            if article[j] not in vocabulary:
                vocabulary[article[j]] = count
                count = count + 1

    # building feature_names
    feature_names = [0] * len(vocabulary)
    for key, value in vocabulary.items():
        feature_names[value] = key

    # building features

    rows, cols = (len(feature_names), len(data))
    features = [[0 for i in range(rows)] for j in range(cols)]

    for i in range(len(data)):
        article = data[i].split()
        for j in range(len(article)):
            for k in range(len(feature_names)):
                article[j] = article[j].capitalize()
                if article[j] == feature_names[k]:
                    features[i][k] += 1

    return {'features': features, 'feature_names': feature_names, 'vocabulary': vocabulary}


fe = feature_extraction(data)

features = fe['features']
feature_names = fe['feature_names']
vocabulary = fe['vocabulary']
print('FEATURES =======================================')
print(features)

# TARGET WISE FEATURES =========================================================

target_wise_features = dict()

for i in range(len(targets)):
    target_wise_features[targets[i]] = []

for i in range(len(targets)):
    target_wise_features[targets[i]].append(
        features[i])

print('TARGET WISE FEATURES ===================================')
print(target_wise_features)

# SUM OF WORDS in EACH CLASS =====================================

total_words = len(feature_names)


sum_of_words_in_articles = target_wise_features

for key, value in target_wise_features.items():
    total = 0

    for i in range(len(value)):
        for j in range(len(value[i])):
            total += value[i][j]
    print('Total', total)

    sum = [0] * len(feature_names)

    for i in range(total_words):
        for j in range(len(value)):
            # print(value[j][i])
            sum[i] += value[j][i]

    print(sum)

    sum_of_words_in_articles[key] = sum

print('SUM OF WORDS =========================================')
print(sum_of_words_in_articles)

# PROB OF EACH WORD IN THAT CLASS ======================================
prob_of_words = sum_of_words_in_articles

for key, value in sum_of_words_in_articles.items():
    total = 0
    for i in range(len(value)):
        total += value[i]

    print('Total', total)
    prob = [0] * len(feature_names)
    for i in range(len(value)):
        prob[i] = value[i] / total

    prob_of_words[key] = prob

print('PROBABILITY OF EACH WORD IN EACH CLASS ==========================')
print(prob_of_words)


# PREDICTING ========================================
test = 'Clean Game'
test_arr = test.split()
print(test_arr)

test_feature_index = [0] * len(test_arr)

# finding word in feature_names
for i in range(len(test_arr)):
    for j in range(len(feature_names)):
        if test_arr[i] == feature_names[j]:
            test_feature_index[i] = j

probability = dict()

for key, value in prob_of_words.items():
    probability[key] = pi[key]
    for i in range(len(test_feature_index)):
        probability[key] *= value[test_feature_index[i]]

print('PROBABILITY =========================')
print(probability)
