# Morphosyntactic tagset convertor
- MULTEXT-East
- Jablonskis 
- Kirtis


Convertor written in python to convert MULTEXT-East tag to Jablonsis accoding to the specs found below.

## Specs
- [MULTEXT-East](./docs/Morf_zymu_standartas_12v-EN.pdf)
- [Jablonskis](./docs/Jablonskis-tagset-EN.pdf)

Original source of the specs is [Lithuanian morphologically annotated corpus - MATAS v1.0](https://clarin.vdu.lt/xmlui/handle/20.500.11821/33)

# Install

```sh
pip install git+https://github.com/aleksas/multext-east-jablonskis-convertor.git
```

## Example

```python

from multext_east_jablonskis_convertor import get_jablonskis_tags

tags = get_jablonskis_tags('Vgmp1s--n--ni-')
print(' '.join(tags))

```
Output
```sh
vksm. asm. tiesiog. es. vns. 1.
```

# TODO
Rewrite using common set of enums. Each conentions should be defined separately from mapping into each other.
