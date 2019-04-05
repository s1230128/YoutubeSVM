import numpy as np


# cosSimularity
# ２つのnumpy型ベクトルのコサイン類似度
def cosSimularity(vec1, vec2):
    innerProduct = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)

    simularity = innerProduct / (norm1 * norm2)

    return simularity
