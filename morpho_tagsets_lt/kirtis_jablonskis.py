from . import sort_jablonskis_tags

jablonskis_kirtis_tag_pairs = [
	('1.', 'Iasm.'),
	('2.', 'IIasm.'),
	('3.', 'IIIasm.'),
	('akr.', ''),
	('arab.', ''),
	('asm.', ''),
	('aukšč.', ''),
	('aukšt.', ''),
	('bdv.', 'bdvr.'),
	('bendr.', 'bendr.gim.'),
	('bev.', 'bevrd.gim.'),
	('bndr.', ''),
	('būdn.', 'būdn.'),
	('būs.', 'būs.l.'),
	('būt-d.', 'būt.d.l.'),
	('būt-k.', 'būt.kart.l.'),
	('būt.', 'būt.l.'),
	('daugin.', 'daugin.'),
	('dgs.', 'dgsk.'),
	('dkt.', 'dktv.'),
	('dll.', 'dll.'),
	('dlv.', 'dlv.'),
	('dvisk.', 'dvisk.'),
	('es.', 'esam.l.'),
	('G.', 'G.'),
	('Il.', 'Vt(ev).'),
	('Įn.', 'Įn.'),
	('išt.', 'ištk.'),
	('įv.', 'įvrd.'),
	('įvardž.', 'įvardž.'),
	('jng.', 'jngt.'),
	('jst.', 'jstk.'),
	('K.', 'K.'),
	('kelint.', 'kelintin.'),
	('kiek.', 'kiekin.'),
	('kita', ''),
	('kuopin.', 'kuopin.'),
	('liep.', ''),
	('mišr.', ''),
	('mot.', 'mot.gim.'),
	('N.', 'N.'),
	('neig.', ''),
	('nelygin.', ''),
	('neveik.', 'neveik.r.'),
	('pad.', 'padlv.'),
	('prl.', 'prln.'),
	('prv.', 'prvks.'),
	('pusd.', 'psdlv.'),
	('raid.', ''),
	('reik.', 'reikiamyb.'),
	('rom.', ''),
	('Š.', 'Š.'),
	('sampl.', ''),
	('sktv.', 'sktv.'),
	('skyr.', ''),
	('sngr.', 'sngr.'),
	('sutr.', 'sutrmp.'),
	('tar.', ''),
	('tęs.', ''),
	('tiesiog.', ''),
	('tikr.', 'T.'),
	('užs.', ''),
	('V.', 'V.'),
	('veik.', 'veik.r.'),
	('vksm.', 'vksm.'),
	('vns.', 'vnsk.'),
	('Vt.', 'Vt.'),
	('vyr.', 'vyr.gim.'),
]

jablonskis_kirtis_opposite_tag_pairs = [
    ('įvardž.', 'neįvardž.'),
    ('sngr.', 'nesngr.')
]

jablonskis_tags = [j for j,k in jablonskis_kirtis_tag_pairs]

jablonskis_categories = [
	'skyr.',
	'dkt.',
	'bdv.',
	'sktv.',
	'įv.',
	'vksm.',
	'prv.',
	'jst.',
	'išt.',
	'dll.',
	'prl.',
	'jng.',
	'akr.',
	'sutr.',
	'tęs.',
	'užs.',
	'kita'
]

fix_jablonskis_string = {
	'būt.k.': 'būt-k.',
	'~DEM.': ''
}

fix_jablonskis_tag_map = {
	'dktv.': 'dkt.',
	'samp.': 'sampl.',
	'kiekin.': 'kiek.',
	'kita.': 'kita',
	'būts.': 'būt.',
	'padlv.': 'pad.',
	'Įv.': 'Įn.',
	'vt.': 'Vt.',
	'būdv.': 'bdv.',
	'nelyg.': 'nelygin.',
	'neygin.': 'nelygin.',
	'v.':'V.'
}
fix_jablonskis_tag_map_key_set = set(fix_jablonskis_tag_map.keys())

jablonskis_verb_form_tag_replacements = {
    'dlv.': ['vksm.', 'dlv.'],
    'pad.': ['vksm.', 'pad..'],
    'pusd.': ['vksm.', 'pusd.'],
    'būdn.': ['vksm.', 'būdn.']
}

valid_jablonskis_tags = [ s for s,_ in jablonskis_kirtis_tag_pairs ]
valid_jablonskis_tag_set = set(valid_jablonskis_tags)

if len(valid_jablonskis_tag_set) != len(valid_jablonskis_tags):
	raise Exception()

kirtis_jablonskis_tag_map = { s:m for m, s in jablonskis_kirtis_tag_pairs }
kirtis_jablonskis_tag_map.update( { s: None for _, s in jablonskis_kirtis_opposite_tag_pairs } )

missing_tags = set([])

def tags_contradict(kirtis_tags, jablonskis_tags):
	for jablonskis_oposite_tag, kirtis_oposite_tag in jablonskis_kirtis_opposite_tag_pairs:
		if kirtis_oposite_tag in kirtis_tags and jablonskis_oposite_tag in jablonskis_tags:
			return True

def kirtis_to_jablonskis_tags(kirtis_tags, jablonskis_tags=None):
	skip = jablonskis_tags and tags_contradict(kirtis_tags, jablonskis_tags)
	
	if not skip:
		tags = []
		for tag in kirtis_tags:
			if tag not in kirtis_jablonskis_tag_map:
				missing_tags.add(tag)
			else:
				if kirtis_jablonskis_tag_map[tag]:
					mapped_tag = kirtis_jablonskis_tag_map[tag]
					if mapped_tag:
						tags.append( mapped_tag )

		sort_jablonskis_tags(tags)
		
		return tags
