<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d0d0d,100:E0182D&height=150&section=header" />

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=15&duration=3000&pause=800&color=E0182D&center=true&vCenter=true&width=520&lines=Cryptography+%26+Protocol+Analysis;Binary+Exploitation+%26+Reverse+Engineering;Systems+Programming+%26+OS+Internals;Network+Security+%26+Embedded+Systems)](https://git.io/typing-svg)

</div>

---

## About

Cybersecurity & Software Engineering student at an **ecole d'ingenieurs**, after a **classe preparatoire aux grandes ecoles (MPI)** -- advanced mathematics, theoretical CS, computability, complexity, formal logic.

I work at the intersection of **systems programming** and **security** -- understanding how things break at the lowest level, and building them right.

Currently studying: cryptography, network security, OS internals, x86 assembly, IoT embedded systems, and formal modelling.

---

## Skills

<div align="center">

[![My Skills](https://skillicons.dev/icons?i=c,python,ocaml,cpp,rust,bash,lua,git,linux,vim,docker&theme=dark)](https://skillicons.dev)

</div>

| Domain | Stack |
|---|----|
| **Languages** | C / Python / OCaml / C++ / x86 ASM / Shell / Lua / *(learning Rust)* |
| **Cybersecurity** | Cryptography / Protocol analysis / Network security / MITM / EBIOS RM |
| **Systems** | OS internals / Proxmox / x86 arch / Logisim / ESP32 / LuaRTOS |
| **Tools** | GCC / GDB / Make / Git / Wireshark / Cisco PT / mitmproxy / Flask |
| **Math** | Number theory / Algorithmic complexity / Formal logic / Mathematical cryptography |

---

## Domains of Interest

<div align="center">

![Cryptography](https://img.shields.io/badge/Cryptography-E0182D?style=for-the-badge&logoColor=white)
![Reverse Engineering](https://img.shields.io/badge/Reverse_Engineering-c0392b?style=for-the-badge&logoColor=white)
![Binary Exploitation](https://img.shields.io/badge/Binary_Exploitation-922b21?style=for-the-badge&logoColor=white)
![Network Security](https://img.shields.io/badge/Network_Security-E0182D?style=for-the-badge&logoColor=white)
![OS Internals](https://img.shields.io/badge/OS_Internals-c0392b?style=for-the-badge&logoColor=white)
![Embedded Systems](https://img.shields.io/badge/Embedded_Systems-922b21?style=for-the-badge&logoColor=white)
![Formal Methods](https://img.shields.io/badge/Formal_Methods-E0182D?style=for-the-badge&logoColor=white)
![x86 Architecture](https://img.shields.io/badge/x86_Architecture-c0392b?style=for-the-badge&logoColor=white)

</div>

---

## Approach

```
$ whoami
  low-level thinker  |  security-first mindset  |  math-driven

$ philosophy
  understand before using  |  break to learn  |  build from scratch

$ env
  linux  |  terminal  |  vim  |  gcc  |  gdb
```

---

## Organizations

| Organization | Focus |
|:---|:---|
| [**dns-114-ctf**](https://github.com/dns-114-ctf) | CTF / binary exploitation / cryptography / reverse |
| [**dns-114-projects**](https://github.com/dns-114-projects) | Academic projects / algorithms / systems / security |
| [**dns-114-academic**](https://github.com/dns-114-academic) | Academic projects / networking / systems / embedded |
| [**dns-114-research**](https://github.com/dns-114-research) | Research / publications / TIPE |

---


<!-- STARS:START -->

## Toolbox

> Repos I follow and use in my workflow.

| Repository | Description | Stars |
|---|---|---|
| [sundowndev/phoneinfoga](https://github.com/sundowndev/phoneinfoga) | Information gathering framework for phone numbers | ⭐ 16,000 |
| [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | Hunt down social media accounts by username across social... | ⭐ 73,593 |
| [wifiphisher/wifiphisher](https://github.com/wifiphisher/wifiphisher) | The Rogue Access Point Framework | ⭐ 14,490 |
| [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei) | Nuclei is a fast, customizable vulnerability scanner powe... | ⭐ 27,430 |
| [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | Ghidra is a software reverse engineering (SRE) framework | ⭐ 65,618 |

<!-- STARS:END -->

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:E0182D,100:0d0d0d&height=100&section=footer" />

</div>

---

## 🗾 Tokyo Map

| | | |
|---|---|---|
| ![](./assets/tokyo1.png) | ![](./assets/tokyo2.png) | ![](./assets/tokyo3.png) |
| ![](./assets/tokyo4.png) | ![](./assets/tokyo5.png) | ![](./assets/tokyo6.png) |


![Tokyo Maps](./assets/tokyo_all.gif)


import { useState } from "react";

const orgs = [
  { name: "dns-114-ctf", focus: "CTF / binary exploitation / cryptography / reverse", emoji: "🔓" },
  { name: "dns-114-projects", focus: "Academic projects / algorithms / systems / security", emoji: "⚙️" },
  { name: "dns-114-academic", focus: "Academic projects / networking / systems / embedded", emoji: "📡" },
  { name: "dns-114-research", focus: "Research / publications / TIPE", emoji: "🔬" },
];

const Tab = ({ label, active, onClick }) => (
  <button
    onClick={onClick}
    style={{
      padding: "8px 20px",
      background: active ? "#E0182D" : "#1a1a1a",
      color: active ? "white" : "#888",
      border: "1px solid " + (active ? "#E0182D" : "#333"),
      cursor: "pointer",
      fontFamily: "monospace",
      fontSize: 13,
      transition: "all 0.2s",
    }}
  >
    {label}
  </button>
);

export default function App() {
  const [tab, setTab] = useState(0);

  return (
    <div style={{ background: "#0d1117", minHeight: "100vh", padding: 32, fontFamily: "monospace", color: "#c9d1d9" }}>
      <div style={{ maxWidth: 700, margin: "0 auto" }}>
        <div style={{ marginBottom: 4, color: "#888", fontSize: 12 }}>APERÇU DU RENDU — choisir un style</div>
        <div style={{ display: "flex", gap: 0, marginBottom: 32 }}>
          {["Badges", "Cards HTML", "Tableau aéré"].map((l, i) => (
            <Tab key={i} label={l} active={tab === i} onClick={() => setTab(i)} />
          ))}
        </div>

        {/* Option 1 : Badges */}
        {tab === 0 && (
          <div>
            <div style={{ color: "#888", fontSize: 11, marginBottom: 16 }}>## Organizations</div>
            <div style={{ display: "flex", flexWrap: "wrap", gap: 10 }}>
              {orgs.map((o) => (
                <div
                  key={o.name}
                  style={{
                    background: "#E0182D",
                    color: "white",
                    padding: "7px 16px",
                    fontSize: 13,
                    fontWeight: "bold",
                    borderRadius: 4,
                    cursor: "pointer",
                    letterSpacing: 0.5,
                  }}
                >
                  {o.name}
                </div>
              ))}
            </div>
            <div style={{ marginTop: 16, color: "#555", fontSize: 11 }}>
              → Compact, rapide à scanner. Pas de description visible directement.
            </div>
          </div>
        )}

        {/* Option 2 : Cards HTML */}
        {tab === 1 && (
          <div>
            <div style={{ color: "#888", fontSize: 11, marginBottom: 16 }}>## Organizations</div>
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
              {orgs.map((o) => (
                <div
                  key={o.name}
                  style={{
                    border: "1px solid #30363d",
                    borderLeft: "3px solid #E0182D",
                    background: "#161b22",
                    padding: "14px 16px",
                    cursor: "pointer",
                  }}
                >
                  <div style={{ color: "#E0182D", fontWeight: "bold", fontSize: 13, marginBottom: 6 }}>
                    {o.emoji} {o.name}
                  </div>
                  <div style={{ color: "#8b949e", fontSize: 11, lineHeight: 1.5 }}>{o.focus}</div>
                </div>
              ))}
            </div>
            <div style={{ marginTop: 16, color: "#555", fontSize: 11 }}>
              → Description visible, visuellement riche. Le plus impactant pour un recruteur.
            </div>
          </div>
        )}

        {/* Option 3 : Tableau aéré */}
        {tab === 2 && (
          <div>
            <div style={{ color: "#888", fontSize: 11, marginBottom: 16 }}>## Organizations</div>
            <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 13 }}>
              <thead>
                <tr style={{ borderBottom: "1px solid #30363d" }}>
                  <th style={{ textAlign: "left", padding: "8px 12px", color: "#888", fontWeight: "normal" }}>Organization</th>
                  <th style={{ textAlign: "left", padding: "8px 12px", color: "#888", fontWeight: "normal" }}>Focus</th>
                </tr>
              </thead>
              <tbody>
                {orgs.map((o, i) => (
                  <tr key={o.name} style={{ borderBottom: "1px solid #21262d", background: i % 2 === 0 ? "transparent" : "#161b22" }}>
                    <td style={{ padding: "12px 12px", color: "#E0182D", fontWeight: "bold" }}>{o.name}</td>
                    <td style={{ padding: "12px 12px", color: "#8b949e" }}>{o.focus}</td>
                  </tr>
                ))}
              </tbody>
            </table>
            <div style={{ marginTop: 16, color: "#555", fontSize: 11 }}>
              → Similaire à l'actuel mais plus lisible. Changement minimal.
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

