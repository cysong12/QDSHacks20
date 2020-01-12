import re
import sys

def lower_case_split(one_element_list):
    return lower_case_iterate(one_element_list[0].split(", "))


def lower_case_iterate(a_list):
    return [elem.lower() for elem in a_list]


def parse_skills(description_value):
    description_value = str(description_value).replace(',', ' ').replace('/', ' ')
    required_skills = set()
    programming_languages_list = ["a#, a-0, a+, a++, abap, abc, acc, accent, ace, "
                                  "action!, actionscript, "
                                  "ada, adenine, agda, agora, aimms, aldor, alef, alf, algol, "
                                  "alice, alma-0, ambienttalk, amos, ampl, "
                                  "angelscript, apex, apl, applescript, apt, arc, arexx, argus, assembly, "
                                  "autohotkey, autolisp, averest, awk, axum, active server pages, "
                                  "b, babbage, ballerina, bc, bcpl, beanshell, bertrand, "
                                  "beta, bliss, blockly, bloop, boo, boomerang, bourne, c, c--, "
                                  "c++, c*, c#, c/al, csh, caml, cayenne, cduce, cecil, cesil, "
                                  "ceylon, cfengine, cg, ch, chapel, charm, chill, chip-8, chomski, chuck, "
                                  "cilk, citrine, cl, claire, clarion, clipper, clips, clojure, clu, cms-2, "
                                  "cobol, cobolscript, cobra, coffeescript, coldfusion, comal, cpl, comit, cil, "
                                  "chr, comtran, coq, coral 66, corvision, cowsel, cryptol, crystal, csound, "
                                  "cuneiform, curl, curry, cybil, cyclone, cython, d, dasl, dart, darwin, dataflex, "
                                  "datalog, datatrieve, dbase, dc, dcl, dinkc, dibol, dog, draco, drakon, dylan, "
                                  "e, ecmascript, egl, eiffel, "
                                  "elan, elixir, elm, emerald, epigram, epl, erlang, es, escher, espol, "
                                  "esterel, euclid, euler, euphoria, "
                                  "cms, ezhil, f, f#, f*, fantom, fish, "
                                  "fl, flavors, flex, floop, flow-matic, focal, foil, formac, forth, "
                                  "fortran, fortress, fp, franz, futhark, f-script, "
                                  "g-code, gdscript, genie, gdl, george, glsl, golang, go!, "
                                  "goal, golo, gödel, gom, google apps script, gosu, gotran, gpss, "
                                  "graphtalk, grasshopper, groovy, haggis, halide, hamilton, "
                                  "harbour, hartmann, haskell, haxe, hermes, hlsl, hollywood, holyc, "
                                  "hopscotch, hugo, hume, hypertalk, irineu, idl, idris, inform, "
                                  "j, j#, j++, jade, jal, janus, jass, java, javafx, javascript, jcl, jean, "
                                  "joss, joule, jovial, joy, jscript, julia, jython, , k, kaleidoscope, karel, "
                                  "kee, kixtart, klerer-may, kif, kojo, kotlin, krc, krl, kuka, krypton, korn, kodu, "
                                  "kv, labview, ladder, lansa, lasso, lava, lc-3, legoscript, lil, lilypond, limbo, "
                                  "limnor, linc, lingo, linq, lis, lisa, lisp, lite-c, lithe, little b, lll,  "
                                  "logtalk, lotuscript, lpc, lse, lsl, livecode, livescript, lua, lucid, lustre, "
                                  "lyapas, lynx, m2001, m4, m#, mad/i, magik, magma, "
                                  "maude, máni, maple, mapper,, mark-iv, mary, masm, math-matic, "
                                  "mathematica, matlab, maxima, max, "
                                  "maxscript, mdl, mercury, mesa, metafont, "
                                  "mheg-5, microcode, microscript, miis, milk, "
                                  "mimic, mirah, miranda, miva, mixal, ml, model 204, modelica, modula, "
                                  "modula-2, modula-3, mohol, moo, mortran, mpd, mathcad, msl, mumps, mupad, mutan, "
                                  "mpl, nasm, napier88, neko, nemerle, .net, nesl, net.data, "
                                  "netlogom, newlisp, newp, newspeak, newtonscript, next generation shell, nial, "
                                  "nice, nickle (nitin), nim, npl, not exactly c (nxc), not quite c (nqc), nsis, nu, "
                                  "nwscript, nxt-g, o:xml, oak, oberon, obj2, object, objectlogo, object rexx, "
                                  "object pascal, objective-c, objective-j, obliq, ocaml, occam, occam-π, octave, omnimark, onyx, "
                                  "opa, opal, opencl, "
                                  "orwell, oxygene, oz, p, pascal, "
                                  "pascal, pcastl, pcf, pearl, peoplecode, perl, pdl, pharo, php, pico, picolisp, "
                                  "plexil, pony, pop-11, pop-2, postscript, pov-ray sdl, powerhouse, "
                                  "powerbuilder, powershell, ppl, "
                                  "processing.js, prograph, proiv, prolog, promal, promela, prose, protel, "
                                  "providex, pro*c, pure data, purescript, python, q, "
                                  "q#, qalb, qtscript, quakec, qpl, qbasic, r, r++, racket, "
                                  "raku, rapid, rapira, ratfiv, ratfor, rc, reason, rebol, red, redcode, refal, rexx, rlab, "
                                  "roop, ruby, rust, s, s2, s3, s-lang, s-plus, sa-c, sabretalk, "
                                  "sail, sam76, sas, sasl, sather, sawzall, scala, scheme, scilab, sed, "
                                  "seed7, sensetalk, sequencel, serpent, setl, simpol, simscript, "
                                  "simula, simulink, singkong, singularity, sisal, slip, smalltalk, sml, strongtalk, "
                                  "snap!, snobol (spitbol), snowball, sol, solidity, sophaeros, spark, speakeasy, "
                                  "speedcode, spin, sp/k, sps, sql, sqr, squeak, squirrel, sr, s/sl, starlogo, strand, "
                                  "stata, stateflow, subtext, sbl, supercollider, supertalk, swift, "
                                  "sympl, systemverilog, t, tacl, tacpol, tads, tal, "
                                  "tcl, tea, teco, telcomp, tex, tie, tmg, toi, topspeed, "
                                  "tpu, trac, ttm, t-sql, ttcn, turing, tutor, txl, typescript, tynker, ubercode, "
                                  "ucsd pascal, umple, unicon, uniface, unity, unix, unrealscript, vala, verilog, "
                                  "vhdl, vim, viper, visual basic, visual dataflex, "
                                  "visual dialogscript, visual fortran, visual foxpro, visual j++, visual lisp, "
                                  "visual objects, visual prolog, vsxu, watfiv, watfor, webassembly, webdna, whiley, "
                                  "winbatch, wolfram language, wyvern, x++, x10, xbase, xbase++, xbl, xc, "
                                  "xharbour, xl, xojo, xotcl, xod, xpath, xpl, xpl0, xquery, xsb, "
                                  "xsharp, xslt, xtend, yorick, yql, yoix, yui, z notation, zebra, zpl, zpl2, zeno, "
                                  "zetalisp, zopl, zsh, zpl, z++"]


    split_programming_languages = lower_case_split(programming_languages_list)
    split_description = [word.lower() for word in description_value.split()]
    for word in split_description:
        if word in split_programming_languages:
            required_skills.add(word)
    return required_skills


def main():
    description = ''.join(sys.argv[1:])
    for skill in parse_skills(description):
        print(skill)


if __name__ == "__main__":
    main()

