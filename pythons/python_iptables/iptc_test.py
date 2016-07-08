#!/usr/bin/env python
# -*- coding: utf-8 -*-
import iptc

table = iptc.Table(iptc.Table.FILTER)
table.autocommit = False
chain = iptc.Chain(table, "INPUT")
for rule in chain.rules:
	if rule.in_interface and "eth0" in rule.in_interface and "DROP" == rule.target.name:
		chain.delete_rule(rule)
table.commit()
table.autocommit = True