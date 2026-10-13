#!/usr/bin/env python3
"""Standard-library structural validation for this skill. Not a scientific correctness validator."""
from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
p=ROOT/'SKILL.md'
if not p.exists(): errors.append('missing SKILL.md')
else:
 t=p.read_text(encoding='utf-8')
 if not t.startswith('---\n'): errors.append('missing YAML frontmatter')
 m=re.search(r'(?m)^name:\s*(.+)$',t)
 d=re.search(r'(?ms)^description:\s*>-\n(.*?)(?=^[a-z][a-z-]*:|^---$)',t)
 if not m or m.group(1).strip()!=ROOT.name: errors.append('skill name != directory')
 if not d: errors.append('missing description')
 for token in ('Human accountability','S00','S17','five meta-level','LICENSE'):
  if token not in t: errors.append('missing contract token '+token)
required=['README.md','README.en.md','AUTHORSHIP.md','LICENSE','CHANGELOG.md','references/resources.md','references/quality-framework.md','playbooks/id/workflow.md','playbooks/en/workflow.md','prompts/id/prompt-pack.md','prompts/en/prompt-pack.md','examples/synthetic-case.md','dist/Research_to_Publication_AI_Skill_v2_Bilingual_All_in_One.md']
for f in required:
 if not (ROOT/f).exists():errors.append('missing '+f)
for f in ['prompts/id/prompt-pack.md','prompts/en/prompt-pack.md']:
 if (ROOT/f).exists():
  x=(ROOT/f).read_text(encoding='utf-8')
  if len(re.findall(r'(?m)^### P\d\d',x))<21:errors.append('too few prompts '+f)
for f in ['playbooks/id/workflow.md','playbooks/en/workflow.md']:
 if (ROOT/f).exists() and 'S17' not in (ROOT/f).read_text(encoding='utf-8'):errors.append('missing S17 '+f)
if errors:
 print('FAIL\n'+'\n'.join(errors));sys.exit(1)
print('PASS: structural bilingual agent-skill checks. Manual legal, scientific and resource review still required.')

