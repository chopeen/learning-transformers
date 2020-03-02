from pprint import pprint

import numpy as np
import tensorflow as tf
from transformers import pipeline

import wikipedia


DOCS = {
    'CAT':   wikipedia.page('Cat').content,
    'TIGER': wikipedia.page('Tiger').content,
    'STAR':  wikipedia.page('Star').content,
    'SUN':   wikipedia.page('Sun').content
}


def main():
    nlp = pipeline('feature-extraction')

    tensors = {
      k: nlp(v)
      for k, v in DOCS.items()
    }

    # Negative quantity between -1 and 0, where 0 indicates orthogonality and
    # values closer to -1 indicate greater similarity
    cosine_loss = tf.keras.losses.CosineSimilarity(axis=1)

    losses = {
      f'{k1}_{k2}': cosine_loss(v1, v2)
      for k1, v1 in tensors.items()
      for k2, v2 in tensors.items()
      if k1 != k2
    }

    pprint(losses)
    '''
    CAT_STAR:   -0.21465103
    CAT_SUN:    -0.20094858
    CAT_TIGER:  -0.2578558
    STAR_SUN:   -0.2681383
    STAR_TIGER: -0.2027754
    SUN_TIGER:  -0.20209934
    '''


'''
   shapes = {
      k: np.squeeze(v).shape
      for k, v in tensors.items()
    }

Why do the tensors have different shapes?

{'CAT':  (106, 768),
 'DOG':  (141, 768),
 'SUN':  ( 75, 768),
 'TREE': (124, 768)}

If the documents are long enough, the squeezed shape is always (512, 768).
'''


if __name__ == '__main__':
    main()