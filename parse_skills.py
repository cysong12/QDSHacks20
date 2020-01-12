import re


def lower_case_split(one_element_list):
    return lower_case_iterate(one_element_list[0].split(", "))


def lower_case_iterate(a_list):
    return [elem.lower() for elem in a_list]


def parse_skills(description_value):
    description_value = description_value.replace(',', ' ')
    required_skills = []
    return_skills_list = []
    programming_languages_list = ["1c, a#, a-0, a+, a++, abap, abc, abc, acc, accent, ace, "
                                  "action!, actionscript, actor, "
                                  "ada, adenine, agda, agilent, agora, aimms, aldor, alef, alf, algol, "
                                  "alice, alma-0, ambienttalk, amiga, amos, ampl, "
                                  "angelscript, apex, apl, applescript, apt, arc, arexx, argus, assembly, "
                                  "autohotkey, autolisp, visual, averest, awk, axum, active server pages, "
                                  "b, babbage, ballerina, bash, basic, bc, bcpl, beanshell, batch, bertrand, "
                                  "beta, bliss, blockly, bloop, boo, boomerang, bourne, c, c--, "
                                  "c++, c plus plus, c*, c#, c/al, csh, c shell, caml, cayenne, cduce, cecil, cesil, "
                                  "ceylon, cfengine, cg, ch, chapel, charity, charm, chill, chip-8, chomski, chuck, "
                                  "cilk, citrine, cl, claire, clarion, clean, clipper, clips, clojure, clu, cms-2, "
                                  "cobol, cobolscript, cobra, coffeescript, coldfusion, comal, cpl, "
                                  "combined programming language, comit, common lisp, cil, constraint handling rules, "
                                  "chr, comtran, cool, coq, coral 66, corvision, cowsel, cryptol, crystal, csound, "
                                  "cuneiform, curl, curry, cybil, cyclone, cython, d, dasl, dart, darwin, dataflex, "
                                  "datalog, datatrieve, dbase, dc, dcl, dinkc, dibol, dog, draco, drakon, dylan, "
                                  "dynamo, dax, e, ease, easytrieve, ec, ecmascript, edinburgh imp, egl, eiffel, "
                                  "elan, elixir, elm, emacs lisp, emerald, epigram, epl, erlang, es, escher, espol, "
                                  "esterel, etoys, euclid, euler, euphoria, euslisp robot programming language, "
                                  "cms, exec, executable, ezhil, f, f#, f*, factor, fantom, faust, ffp, fish, "
                                  "fl, flavors, flex, floop, flow-matic, focal, focus, foil, formac, @formula, forth, "
                                  "fortran, fortress, fp, franz, futhark, f-script, game maker language, "
                                  "gamemonkey, gams, g-code, gdscript, genie, gdl, george, glsl, gnu, go, go!, "
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
                                  "Mathematica, MATLAB, Maxima, Max, "
                                  "MaxScript, MDL, Mercury, Mesa, Metafont, "
                                  "MHEG-5, Microcode, MicroScript, MIIS, Milk, "
                                  "MIMIC, Mirah, Miranda, MIVA Script, MIVA, Mixal, ML, Model 204, Modelica, Modula, "
                                  "Modula-2, Modula-3, Mohol, MOO, Mortran, Mouse, MPD, Mathcad, MSL, MUMPS, muPAD, Mutan, "
                                  "MPL, NASM, Napier88, Neko, Nemerle, NESL, Net.Data, "
                                  "NetLogom, NewLISP, NEWP, Newspeak, NewtonScript, Next Generation Shell, Nial, "
                                  "Nice, Nickle (NITIN), Nim, NPL, Not eXactly C (NXC), Not Quite C (NQC), NSIS, Nu, "
                                  "NWScript, NXT-G, o:XML, Oak, Oberon, OBJ2, Object, ObjectLOGO, Object REXX, "
                                  "Object Pascal, Objective-C, Objective-J, Obliq, OCaml, occam, occam-π, Octave, OmniMark, Onyx, "
                                  "Opa, Opal, OpenCL, OpenEdge, OPL, OpenVera, OPS5OptimJ, Orc, ORCA/Modula-2, Oriel, "
                                  "Orwell, Oxygene, Oz, P, P4, P′′, ParaSail, PARI/GP, Pascal, "
                                  "Pascal, PCASTL, PCF, PEARL, PeopleCode, Perl, PDL, Pharo, PHP, Pico, Picolisp, "
                                  "Pict, Pig, Pike, PILOT, Pipelines, Pinecone, Pizza, PL-11, PL/0, "
                                  "PL/B, PL/C, PL/I – ISO 6160, PL/M, PL/P, PL/SQL, PL360, PLANC, Plankalkül, Planner, PLEX, "
                                  "PLEXIL, Plus, Pony, POP-11, POP-2, PostScript, PortablE, POV-Ray SDL, Powerhouse, "
                                  "PowerBuilder, PowerShell, PPL, Processing, "
                                  "Processing.js, Prograph, PROIV, Prolog, PROMAL, Promela, PROSE, PROTEL, "
                                  "ProvideX, Pro*C, Pure, Pure Data, PureScript, Python, Q, "
                                  "Q#, Qalb, QtScript, QuakeC, QPL, Qbasic, R, R++, Racket, "
                                  "Raku, RAPID, Rapira, Ratfiv, Ratfor, rc, Reason, REBOL, Red, Redcode, REFAL, REXX, Rlab, "
                                  "ROOP, RPG, RPL, RSL, RTL/2, Ruby, Rust, S, S2, S3, S-Lang, S-PLUS, SA-C, SabreTalk, "
                                  "SAIL, SAM76, SAS, SASL, Sather, Sawzall, Scala, Scheme, Scilab, Scratch, Script.NET, Sed, "
                                  "Seed7, Self, SenseTalk, SequenceL, Serpent, SETL, SIMPOL, SIGNAL, SiMPLE, SIMSCRIPT, "
                                  "Simula, Simulink, Singkong, Singularity, SISAL, SLIP, SMALL, Smalltalk, SML, Strongtalk, "
                                  "Snap!, SNOBOL (SPITBOL), Snowball, SOL, Solidity, SOPHAEROS, Source, SPARK, Speakeasy, "
                                  "Speedcode, SPIN, SP/k, SPS, SQL, SQR, Squeak, Squirrel, SR, S/SL, Starlogo, Strand, "
                                  "Stata, Stateflow, Subtext, SBL, SuperCollider, SuperTalk, Swift, "
                                  "Swift (parallel scripting language), SYMPL, SystemVerilog, T, TACL, TACPOL, TADS, TAL, "
                                  "Tcl, Tea, TECO, TELCOMP, TeX, TIE, TMG, compiler-compiler, Tom, TOM, Toi, Topspeed, "
                                  "TPU, Trac, TTM, T-SQL, Transcript, TTCN, Turing, TUTOR, TXL, TypeScript, Tynker, Ubercode, "
                                  "UCSD Pascal, Umple, Unicon, Uniface, UNITY, Unix, UnrealScript, Vala, Verilog, "
                                  "VHDL, Vim, Viper, Visual, Visual Basic .NET, Visual DataFlex, "
                                  "Visual DialogScript, Visual Fortran, Visual FoxPro, Visual J++, Visual LISP, "
                                  "Visual Objects, Visual Prolog, VSXu, WATFIV, WATFOR, WebAssembly, WebDNA, Whiley, "
                                  "Winbatch, Wolfram Language, Wyvern, X++, X10, xBase, xBase++, XBL, XC (targets XMOS architecture), "
                                  "xHarbour, XL, Xojo, XOTcl, XOD (programming language), XPath, XPL, XPL0, XQuery, XSB, "
                                  "XSharp, XSLT, Xtend, Yorick, YQL, Yoix, YUI, Z notation, Zebra, ZPL, ZPL2, Zeno, "
                                  "ZetaLisp, ZOPL, Zsh, ZPL, Z++"]

    two_word_skills = ["a#", 'a-0', 'abc', 'ace', 'agilent', 'aimms', 'algol', 'assembly', 'batch', 'bourne', 'common',
                       'easy', 'edinburgh', 'emacs', 'exec', 'cms', 'executable', 'gnu', 'gamemonkey', 'hartmann',
                       'ibm', 'javafx', 'join', 'jscript', 'korn', 'klerer-may', 'maude', 'miva', 'object', 'openedge',
                       'pascal', 'unix','ucsd', 'vim', 'visual', 'z']

    programming_languages_lower_case_split_list = lower_case_split(programming_languages_list)
    print(programming_languages_lower_case_split_list)
    orig_words_split = description_value.split()
    split_description = [word.lower() for word in description_value.split()]
    print(split_description)
    print(orig_words_split)
    for word in split_description:
        if word in programming_languages_lower_case_split_list:
            required_skills.append(word)
    for skill in required_skills:
        if skill in two_word_skills:
            return_skills_list.append(orig_words_split[split_description.index(skill)] + ' ' +
                                      orig_words_split[split_description.index(skill) + 1])
        else:
            return_skills_list.append(orig_words_split[split_description.index(skill)])
    return return_skills_list


def main():
    job_description = "Required skills: C, C++, and exposure to a# .NET and some vim script"
    print(parse_skills(job_description))


if __name__ == "__main__":
    main()