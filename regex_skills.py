import re


def lower_case_split(one_element_list):
    return lower_case_iterate(one_element_list[0].split(", "))


def lower_case_iterate(a_list):
    return [elem.lower() for elem in a_list]


def two_words_reference(a_word):
    two_words_programming_language = {}
    return two_words_programming_language[a_word]

def parse_skills(description_value):
    description_value = description_value.replace(',', ' ')
    required_skills = []
    programming_languages_list = ["1c, a, a-0 system, a+, a++, abap, abc, abc algol, acc, accent, ace dasl, "
                                  "distributed application specification language, action!, actionscript, actor, "
                                  "ada, adenine, agda, agilent vee, agora, aimms, aldor, alef, alf, algol 58, "
                                  "algol 60, algol 68, algol w, alice, alma-0, ambienttalk, amiga e, amos, ampl, "
                                  "angelscript, apex, apl, applescript, apt, arc, arexx, argus, assembly language, "
                                  "autohotkey, autolisp, visual lisp, averest, awk, axum, active server pages, "
                                  "b, babbage, ballerina, bash, basic, bc, bcpl, beanshell, batch file, bertrand, "
                                  "beta, bliss, blockly, bloop, boo, boomerang, bourne shell, c, c--, c minus minus, "
                                  "c++, c plus plus, c*, c#, c/al, csh, c shell, caml, cayenne, cduce, cecil, cesil, "
                                  "ceylon, cfengine, cg, ch, chapel, charity, charm, chill, chip-8, chomski, chuck, "
                                  "cilk, citrine, cl, claire, clarion, clean, clipper, clips, clojure, clu, cms-2, "
                                  "cobol, cobolscript, cobra, coffeescript, coldfusion, comal, cpl, "
                                  "combined programming language, comit, common lisp, cil, constraint handling rules, "
                                  "chr, comtran, cool, coq, coral 66, corvision, cowsel, cryptol, crystal, csound, "
                                  "cuneiform, curl, curry, cybil, cyclone, cython, d, dasl, dart, darwin, dataflex, "
                                  "datalog, datatrieve, dbase, dc, dcl, dinkc, dibol, dog, draco, drakon, dylan, "
                                  "dynamo, dax, e, ease, easytrieve plus, ec, ecmascript, edinburgh imp, egl, eiffel, "
                                  "elan, elixir, elm, emacs lisp, emerald, epigram, epl, erlang, es, escher, espol, "
                                  "esterel, etoys, euclid, euler, euphoria, euslisp robot programming language, "
                                  "cms exec, exec, executable uml, ezhil, f, f#, f*, factor, fantom, faust, ffp, fish, "
                                  "fl, flavors, flex, floop, flow-matic, focal, focus, foil, formac, @formula, forth, "
                                  "fortran, fortress, fp, franz lisp, futhark, f-script, game maker language, "
                                  "gamemonkey script, gams, g-code, gdscript, genie, gdl, george, glsl, gnu e, go, go!, "
                                  "goal, golo, gödel, gom, good old mad, google apps script, gosu, gotran, gpss, "
                                  "graphtalk, grass, grasshopper, groovy, hack, haggis, hal/s, halide, hamilton, "
                                  "harbour, hartmann, haskell, haxe, hermes, high, hlsl, hollywood, holyc, hop, "
                                  "hopscotch, hope, hugo, hume, hypertalk, io, icon, ibm, irineu, idl, idris, inform, "
                                  "j, j#, j++, jade, jal, janus, jass, java, javafx, javascript, jcl, jean, join, "
                                  "joss, joule, jovial, joy, jscript, julia, jython, , k, kaleidoscope, karel, "
                                  "kee, kixtart, klerer-may, kif, kojo, kotlin, krc, krl, kuka, krypton, korn, kodu, "
                                  "kv, labview, ladder, lansa, lasso, lava, lc-3, legoscript, lil, lilypond, limbo, "
                                  "limnor, linc, lingo, linq, lis, lisa, lisp, lite-c, lithe, little b, lll, logo, "
                                  "logtalk, lotuscript, lpc, lse, lsl, livecode, livescript, lua, lucid, lustre, "
                                  "lyapas, lynx, m2001, m4, m#, machine, mad, michigan, mad/i, magik, magma, "
                                  "Maude, Máni, Maple, MAPPER,, MARK-IV, Mary, MASM, microsoft, MATH-MATIC, "
                                  "Mathematica, MATLAB, Maxima (see also Macsyma), Max (Max Msp – Graphical Programming Environment), "
                                  "MaxScript internal language 3D Studio Max, Maya (MEL), MDL, Mercury, Mesa, Metafont, "
                                  "MHEG-5 (Interactive TV programming language), Microcode, MicroScript, MIIS, Milk (programming language), "
                                  "MIMIC, Mirah, Miranda, MIVA Script, MIVA Script, Mixal, ML, Model 204, Modelica, Modula, "
                                  "Modula-2, Modula-3, Mohol, MOO, Mortran, Mouse, MPD, Mathcad, MSL, MUMPS, muPAD, Mutan, "
                                  "Mystic Programming Language (MPL), NASM, Napier88, Neko, Nemerle, NESL, Net.Data, "
                                  "NetLogom NetRexx, NewLISP, NEWP, Newspeak, NewtonScript, Next Generation Shell, Nial, "
                                  "Nice, Nickle (NITIN), Nim, NPL, Not eXactly C (NXC), Not Quite C (NQC), NSIS, Nu, "
                                  "NWScript, NXT-G, o:XML, Oak, Oberon, OBJ2, Object Lisp, ObjectLOGO, Object REXX, "
                                  "Object Pascal, Objective-C, Objective-J, Obliq, OCaml, occam, occam-π, Octave, OmniMark, Onyx, "
                                  "Opa, Opal, OpenCL, OpenEdge ABL, OPL, OpenVera, OPS5OptimJ, Orc, ORCA/Modula-2, Oriel, "
                                  "Orwell, Oxygene, Oz, P, P4, P′′, ParaSail (programming language), PARI/GP, Pascal – ISO 7185, "
                                  "Pascal Script, PCASTL, PCF, PEARL, PeopleCode, Perl, PDL, Pharo, PHP, Pico, Picolisp, "
                                  "Pict, Pig (programming tool), Pike, PILOT, Pipelines, Pinecone, Pizza, PL-11, PL/0, "
                                  "PL/B, PL/C, PL/I – ISO 6160, PL/M, PL/P, PL/SQL, PL360, PLANC, Plankalkül, Planner, PLEX, "
                                  "PLEXIL, Plus, Pony, POP-11, POP-2, PostScript, PortablE, POV-Ray SDL, Powerhouse, "
                                  "PowerBuilder – 4GL GUI application generator from Sybase, PowerShell, PPL, Processing, "
                                  "Processing.js, Prograph, PROIV, Prolog, PROMAL, Promela, PROSE modeling language, PROTEL, "
                                  "ProvideX, Pro*C, Pure, Pure Data, PureScript, Python, Q (programming language from Kx Systems), "
                                  "Q# (Microsoft programming language), Qalb, QtScript, QuakeC, QPL, Qbasic, R, R++, Racket, "
                                  "Raku, RAPID, Rapira, Ratfiv, Ratfor, rc, Reason, REBOL, Red, Redcode, REFAL, REXX, Rlab, "
                                  "ROOP, RPG, RPL, RSL, RTL/2, Ruby, Rust, S, S2, S3, S-Lang, S-PLUS, SA-C, SabreTalk, "
                                  "SAIL, SAM76, SAS, SASL, Sather, Sawzall, Scala, Scheme, Scilab, Scratch, Script.NET, Sed, "
                                  "Seed7, Self, SenseTalk, SequenceL, Serpent, SETL, SIMPOL, SIGNAL, SiMPLE, SIMSCRIPT, "
                                  "Simula, Simulink, Singkong, Singularity, SISAL, SLIP, SMALL, Smalltalk, SML, Strongtalk, "
                                  "Snap!, SNOBOL (SPITBOL), Snowball, SOL, Solidity, SOPHAEROS, Source, SPARK, Speakeasy, "
                                  "Speedcode, SPIN, SP/k, SPS, SQL, SQR, Squeak, Squirrel, SR, S/SL, Starlogo, Strand, "
                                  "Stata, Stateflow, Subtext, SBL, SuperCollider, SuperTalk, Swift (Apple programming language), "
                                  "Swift (parallel scripting language), SYMPL, SystemVerilog, T, TACL, TACPOL, TADS, TAL, "
                                  "Tcl, Tea, TECO, TELCOMP, TeX, TIE, TMG, compiler-compiler, Tom, TOM, Toi, Topspeed, "
                                  "TPU, Trac, TTM, T-SQL, Transcript, TTCN, Turing, TUTOR, TXL, TypeScript, Tynker, Ubercode, "
                                  "UCSD Pascal, Umple, Unicon, Uniface, UNITY, Unix shell, UnrealScript, Vala, Verilog, "
                                  "VHDL, Vim script, Viper, Visual Basic, Visual Basic .NET, Visual DataFlex, "
                                  "Visual DialogScript, Visual Fortran, Visual FoxPro, Visual J++, Visual LISP, "
                                  "Visual Objects, Visual Prolog, VSXu, WATFIV, WATFOR, WebAssembly, WebDNA, Whiley, "
                                  "Winbatch, Wolfram Language, Wyvern, X++, X10, xBase, xBase++, XBL, XC (targets XMOS architecture), "
                                  "xHarbour, XL, Xojo, XOTcl, XOD (programming language), XPath, XPL, XPL0, XQuery, XSB, "
                                  "XSharp, XSLT, Xtend, Yorick, YQL, Yoix, YUI, Z notation, Zebra, ZPL, ZPL2, Zeno, "
                                  "ZetaLisp, ZOPL, Zsh, ZPL, Z++"]

    programming_languages_lower_case_split_list = lower_case_split(programming_languages_list)
    print(programming_languages_lower_case_split_list)

    split_description = description_value.split()
    for word in split_description:
        # print(word)
        if word in programming_languages_lower_case_split_list:
            # print(word, word in programming_languages_list)
            required_skills.append(word)
    # print(required_skills)
    return required_skills


def main():
    job_description = "Required skills: c, c++, and exposure to emacs"
    print(parse_skills(job_description))


if __name__ == "__main__":
    main()
