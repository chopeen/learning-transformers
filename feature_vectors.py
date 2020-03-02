from pprint import pprint

import numpy as np
import tensorflow as tf
from transformers import pipeline


DOCS = {
    'CAT': 'The cat (Felis catus) is a small carnivorous mammal. It is the only domesticated species in the family Felidae and often referred to '
    'as the domestic cat to distinguish it from wild members of the family. The cat is either a house cat, a farm cat or a feral cat; '
    'latter ranges freely and avoids human contact. Domestic cats are valued by humans for companionship and for their ability to hunt '
    'rodents. About 60 cat breeds are recognized by various cat registries.',
    'DOG': 'The domestic dog (Canis lupus familiaris when considered a subspecies of the wolf or Canis familiaris when considered a distinct '
    'species) is a mammal, a member of the genus Canis (canines), which forms part of the wolf-like canids, and is the most widely '
    'abundant terrestrial carnivore. The dog and the extant gray wolf are sister taxa as modern wolves are '
    'not closely related to the wolves that were first domesticated, which implies that the direct ancestor of the dog is extinct. '
    'The dog was the first species to be domesticated, and has been selectively bred over millennia for various behaviors, sensory '
    'capabilities, and physical attributes.',
    'TREE': 'In botany, a tree is a perennial plant with an elongated stem, or trunk, supporting branches and leaves in most species. '
    'In some usages, the definition of a tree may be narrower, including only woody plants with secondary growth, plants that are usable '
    'as lumber or plants above a specified height. In wider definitions, the taller palms, tree ferns, bananas, and bamboos are also trees. '
    'Trees are not a taxonomic group but include a variety of plant species that have independently evolved a trunk and branches as a way '
    'to tower above other plants to compete for sunlight.',
    'SUN': 'The Sun is a G-type main-sequence star (G2V) based on its spectral class. As such, it is informally and not completely accurately '
    'referred to as a yellow dwarf (its light is closer to white than yellow). It formed approximately 4.6 billion years ago from '
    'the gravitational collapse of matter within a region of a large molecular cloud.'
}


def main():
    nlp = pipeline('feature-extraction')

    tensors = {
      k: nlp(v)
      for k, v in DOCS.items()
    }

    # FIXME: Does it make sense to slice the tensors in order to normalize them?
    tensors_sliced = {
      k: np.squeeze(v)[:75]
      for k, v in tensors.items()
    }

    # Negative quantity between -1 and 0, where 0 indicates orthogonality and
    # values closer to -1 indicate greater similarity
    cosine_loss = tf.keras.losses.CosineSimilarity(axis=1)

    losses = {
      f'{k1}_{k2}': cosine_loss(v1, v2)
      for k1, v1 in tensors_sliced.items()
      for k2, v2 in tensors_sliced.items()
      if k1 != k2
    }

    pprint(losses)


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
'''


if __name__ == '__main__':
    main()