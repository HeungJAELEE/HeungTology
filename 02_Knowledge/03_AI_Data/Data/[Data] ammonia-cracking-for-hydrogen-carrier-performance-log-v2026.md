---
lineage:
  dataset_reference: ammonia-cracking-for-hydrogen-carrier-performance-log-v2026
  original_author: Antigravity_Agent_Flash_Offline
  original_hash: auto_generated
measurement:
  confidence_interval:
  - 0.0
  - 0.0
  instrument: Heuristic_Regex_Parser
  precision: '0.0'
  unit: Recovery (%)
  value: 22734
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-24'
  domain: 03_AI_Data
  id: '[[ [03_AI_Data] [Data] ammonia-cracking-for-hydrogen-carrier-performance-log-v2026]]'
  last_updated: '2026-05-24T02:50:00+09:00'
  project: Antigravity_SDF_Core
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Auto-parsed Data node for ammonia-cracking-for-hydrogen-carrier-performance-log-v2026
  object_type: Data
  tier: 1
properties:
  co_conversion_min_pct: 90.0
  co_reaction_temp_range_c: 500-650
  enthalpy_of_decomposition_kj_mol: 46.2
  ni_conversion_min_pct: 95.0
  ni_reaction_temp_range_c: 600-750
  residual_nh3_limit_ppm: 0.1
  ru_activation_energy_reduction_pct: 30.0
  ru_conversion_min_pct: 99.9
  ru_reaction_rate_increase_factor: 5.0
  ru_reaction_temp_range_c: 400-550
  solar_thermal_min_temp_c: 800
semantic:
  alternative_parents: []
  is_instance_of: '[[ [03_AI_Data] [Concept] ammonia-cracking-for-hydrogen-carrier-performance-log-v2026]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: automated_categorization
  object: Data
  predicate: auto_mapped
  subject: ammonia-cracking-for-hydrogen-carrier-performance-log-v2026
  weight: 0.4
temporal:
  valid_from: '2026-05-24T02:50:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.05
  t_static: 0.8
validation:
  last_validated: '2026-05-24T02:50:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Data] Ammonia Cracking For Hydrogen Carrier Performance Log V2026

## 1. [Executive Summary: Hydrogen Liberation via $NH_3$ Cracking]
Hydrogen's low volumetric energy density necessitates the utilization of Ammonia ($NH_3$) as a high-capacity chemical carrier [데이터 부재]. This log documents the critical conversion parameters required to liberate $H_2$ from the nitrogen-bonded state to ensure fuel cell integrity and supply chain economic viability. The primary technical objective is the optimization of cracking efficiency and the absolute minimization of residual $NH_3$ to prevent PEMFC catalyst poisoning [데이터 부재].

## 2. [Technical Specifications: Catalyst & Reaction Parameters]

### 2.1 [Catalyst Performance Matrix (v2026)]

| Catalyst Type | Reaction Temp ($^\circ C$) [데이터 부재] | Conversion (%) [데이터 부재] | $H_2$ Recovery (%) [데이터 부재] | Residual $NH_3$ (ppm) [데이터 부재] | Rationale |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Ruthenium (Ru/Al2O3)** | $400 \sim 550$ | $> 99.9$ | $90 \sim 95$ | $< 0.1$ | High-activity / Low-temp [데이터 부재] |
| **Nickel (Ni-based)** | $600 \sim 750$ | $95 \sim 99$ | $85 \sim 92$ | $1 \sim 10$ | Cost-effective / Mass-scale [데이터 부재] |
| **Cobalt (Co-based)** | $500 \sim 650$ | $90 \sim 98$ | $80 \sim 90$ | $5 \sim 20$ | REE-reduction Alternative [데이터 부재] |
| **Electrochemical** | $Ambient$ | Variable | Variable | N/A | Zero-heat Direct Dissociation |
| **Solar-Thermal** | $> 800$ | $> 99$ | Stable | $< 1$ | Carbon-zero Thermal Integration |

### 2.2 [Performance Comparison: Theoretical vs. Verified]

| Parameter | Theoretical Value (Ideal) | Verified Value (Empirical) | Deviation/Margin |
| :--- | :---: | :---: | :---: |
| $NH_3$ Conversion (Ru) | $100.0\%$ | $> 99.9\%$ [데이터 부재] | $< 0.1\%$ |
| $NH_3$ Conversion (Ni) | $100.0\%$ | $95.0 \sim 99.0\%$ [데이터 부재] | $1.0 \sim 5.0\%$ |
| Residual $NH_3$ Limit | $0.0 \text{ ppm}$ | $< 0.1 \text{ ppm}$ [데이터 부재] | $0.1 \text{ ppm}$ |
| $H_2$ Recovery (Standard) | $100.0\%$ | $85.0 \sim 95.0\%$ [데이터 부재] | $5.0 \sim 15.0\%$ |

## 3. [Scientific Rationale: Thermodynamics & Kinetics]

### 3.1 [Endothermic Equilibrium Model]
The decomposition reaction is governed by the following equilibrium:
$$ 2NH_3 \rightleftharpoons N_2 + 3H_2, \quad \Delta H^0 = 46.2 \text{ kJ/mol} \text{ [데이터 부재]} $$
Higher temperatures shift the equilibrium towards $H_2$ production; however, thermal uniformity within the reactor is mandatory to prevent conversion localized drops [데이터 부재].

### 3.2 [Kinetics & Activation Energy]
Ruthenium ($Ru$) catalysts exhibit an activation energy ($E_a$) approximately $30\%$ lower than Nickel ($Ni$) based catalysts, resulting in a $\sim 5\times$ increase in reaction rate at identical operating temperatures [데이터 부재].

## 4. [Failure Mode & Risk Analysis]

### 4.1 [Catalyst Poisoning: $NH_3$ Slip]
Residual $NH_3$ concentrations exceeding $0.1 \text{ ppm}$ [데이터 부재] induce irreversible poisoning of Platinum (Pt) active sites in PEMFC stacks, leading to a projected $50\%$ reduction in stack lifespan via site-blocking mechanisms [데이터 부재].

### 4.2 [Energy Efficiency: Heat Integration]
Systemic efficiency is highly dependent on waste heat recovery. Integrating cracker exhaust gas with inlet $NH_3$ preheating can improve total system efficiency by $15\%$ [데이터 부재].

## 5. [Integrity Audit Logic: Ammonia-to-Hydrogen Transition]

```python
# [Operational Auditor] Ammonia Cracking & Hydrogen Liberation
def audit_ammonia_cracking(reactor_temp_sensors, inlet_nh3_flow, outlet_h2_purity):
    # 1. Conversion Rate Audit via Thermal Profile
    avg_temp = calculate_weighted_average(reactor_temp_sensors)
    expected_conversion = estimate_conversion_from_temp(avg_temp, catalyst_type)
    if avg_temp < MIN_CRACKING_TEMP:
        status = "INCOMPLETE_DECOMPOSITION_RISK"
        action = "INCREASE_BURNER_OUTPUT"
        
    # 2. Residual NH3 (Poisoning Risk) Audit
    current_nh3_ppm = outlet_h2_purity.residual_nh3_ppm
    if current_nh3_ppm > 0.1: # [데이터 부재]
        status = "AMMONIA_SLIP_POISONING_DANGER"
        action = "TRIGGER_PURIFICATION_RECALIBRATION"
    
    # 3. Specific Energy Intensity Audit
    energy_intensity = calculate_energy_input() / measure_h2_yield()
    if energy_intensity > ENERGY_SPEC_LIMIT:
        status = "THERMAL_INEFFICIENCY_DETECTED"
        action = "OPTIMIZE_WASTE_HEAT_RECOVERY"
        
    return {"status": status, "h2_purity": outlet_h2_purity.h2_content, "action": action}
```

## 6. [Self-Check Validation]
1. **Thermodynamics**: Calculate the stoichiometric expansion ratio of $2NH_3 \to N_2 + 3H_2$. (Ans: $4/2 = 2.0\times$)
2. **Safety**: Identify the maximum permissible residual $NH_3$ concentration for PEMFC applications. (Ans: $0.1 \text{ ppm}$ [데이터 부재])
3. **Efficiency**: Evaluate the impact of $E_a$ reduction on reactor throughput using the Arrhenius relationship.

### 🔗 Retrieved Knowledge Nodes
- MOC 22_hydrogen-economy-and-fuel-cells-intelligence-hub
- Data liquid-hydrogen-evaporation-boil-off-rate-bor-log-v2026
- Data pem-fuel-cell-stack-efficiency-and-voltage-degradation-log-v2026
- [SOP] ammonia-cracking-reactor-startup-and-catalyst-activation-procedure