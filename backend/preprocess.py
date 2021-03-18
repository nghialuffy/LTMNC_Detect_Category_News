import regex as re
from tqdm import tqdm
from core import remove_stopwords, text_preprocess


# # Create stop word
# total_label = 18
# vocab = {}
# label_vocab = {}
# for line in open('./data/raw_data.txt'):
#     words = line.split()
#     # lưu ý từ đầu tiên là nhãn
#     label = words[0]
#     if label not in label_vocab:
#         label_vocab[label] = {}
#     for word in words[1:]:
#         label_vocab[label][word] = label_vocab[label].get(word, 0) + 1
#         if word not in vocab:
#             vocab[word] = set()
#         vocab[word].add(label)

# count = {}
# for word in vocab:
#     if len(vocab[word]) == total_label:
#         count[word] = min([label_vocab[x][word] for x in label_vocab])
        
# sorted_count = sorted(count, key=count.get, reverse=True)
# with open('./data/stop_words.txt', 'r') as fp:
#     for word in sorted_count[:200]:
#         stopword.add(word)
#         fp.write(word + '\n')


# Remove stop words
print("Create new")
with open('./data/new_data.txt', 'w') as fp:
    for line in tqdm(open('./data/raw_data.txt')):
        label = line.split(" ")[0]
        text = line.replace(label, "")
        text = text_preprocess(text)
        fp.write(label + " " + text + '\n')
