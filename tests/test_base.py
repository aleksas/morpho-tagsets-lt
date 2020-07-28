#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, main
import multext_east_jablonskis_convertor.multext_east_jablonskis as mej

noun_cases = [
    ('Lietuvai', 'Npfsdng'),
    ('vasarą', 'Ncfsan-'),
    ('bankuchenas', 'Nnmsgn-')
]

verb_cases = [
    ('rezervuoju', 'Vgmp1s--n--ni-'),
    ('paliktu', 'Vgps-smpnnin-p'),
    ('bėgte', 'Vgb-----n--n--')
]

adjective_cases = [
    ('svarbu', 'Agpn--n'),
    ('gražiausius', 'Agsmpan'),
    ('biednas', 'Anpmsnn')
]

pronoun_cases = [
    ('visoks', 'Pgmpin'),
    ('man', 'Pg-sdn'),
    ('toooks', 'Pgmsnn') # !DOC ISSUE: Pnmsnn > Pgmsnn
]

numeral_cases = [
    ('penkiom', 'Mcf-iln'), ('penkiom', 'Mcf-dln'),
    ('10', 'M----d-'),
    ('pem', 'Mn-----')
]

adverb_cases = [
    ('apskritai', 'Rgp'),
    ('geriau', 'Rgc')
]

preposition_cases = [
    ('su', 'Sgi'),
    ('po','Sgg'), ('po','Sga'), ('po','Sgi')
]

conjunction_cases = [
    ('būtent', 'Cg'),
    ('ir', 'Cg')
]

tests = [
    (noun_cases, mej.noun),
    (verb_cases, mej.verb),
    (adjective_cases, mej.adjective),
    (pronoun_cases, mej.pronoun),
    (numeral_cases, mej.numeral),
    (adverb_cases, mej.adverb),
    (preposition_cases, mej.preposition),
    (conjunction_cases, mej.conjunction)
]

class SimpleTestCase(TestCase):
    def test_1(self):
        for cases, category in tests:
            for case in cases:
                tags = list(mej.get_jablonskis_tags(case[1]))
                category_tag = list(category[0].values())[0]
                if category_tag not in tags:
                    raise Exception()

if __name__ == '__main__':
    main()