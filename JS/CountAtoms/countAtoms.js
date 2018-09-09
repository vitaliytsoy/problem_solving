  function parseMolecule(formula) {
    let atomsAmount = {}
    let multiplier_1 = 1;
    let multiplier_2 = 1;
    let multiplier_3 = 1;
    let re = new RegExp('(H[0-9]*|Li[0-9]*|Be[0-9]*|Na[0-9]*|K[0-9]*|Rb[0-9]*|Cs[0-9]*|Fr[0-9]*|Uue[0-9]*|Be[0-9]*|Mg[0-9]*|Ca[0-9]*|Sr[0-9]*|Ba[0-9]*|Ra[0-9]*|Ubn[0-9]*|Sc[0-9]*|Y[0-9]*|Ti[0-9]*|Zr[0-9]*|Hf[0-9]*|Rf[0-9]*|V[0-9]*|Nb[0-9]*|Ta[0-9]*|Db[0-9]*|Cr[0-9]*|Mo[0-9]*|W[0-9]*|Sg[0-9]*|Mn[0-9]*|Tc[0-9]*|Re[0-9]*|Bh[0-9]*|Fe[0-9]*|Ru[0-9]*|Os[0-9]*|Hs[0-9]*|Co[0-9]*|Rh[0-9]*|Pd[0-9]*|Pt[0-9]*|Ds[0-9]*|Cu[0-9]*|Ag[0-9]*|Au[0-9]*|Rg[0-9]*|Zn[0-9]*|Cd[0-9]*|Hg[0-9]*|Cn[0-9]*|B[0-9]*|Al[0-9]*|Ga[0-9]*|In[0-9]*|Tl[0-9]*|Nh[0-9]*|C[0-9]*|Si[0-9]*|Ge[0-9]*|Sn[0-9]*|Pb[0-9]*|Fl[0-9]*|N[0-9]*|P[0-9]*|As[0-9]*|Sb[0-9]*|Bi[0-9]*|Mc[0-9]*|O[0-9]*|S[0-9]*|Se[0-9]*|Te[0-9]*|Po[0-9]*|Lv[0-9]*|F[0-9]*|Cl[0-9]*|Br[0-9]*|I[0-9]*|At[0-9]*|Ts[0-9]*|He[0-9]*|Ne[0-9]*|Ar[0-9]*|Kr[0-9]*|Xe[0-9]*|Rn[0-9]*|Og[0-9]*|La[0-9]*|Ce[0-9]*|Pr[0-9]*|Nd[0-9]*|Pm[0-9]*|Sm[0-9]*|Eu[0-9]*|Gd[0-9]*|Tb[0-9]*|Dy[0-9]*|Ho[0-9]*|Er[0-9]*|Tm[0-9]*|Yb[0-9]*|Lu[0-9]*|Ac[0-9]*|Th[0-9]*|Pa[0-9]*|U[0-9]*|Np[0-9]*|Pu[0-9]*|Am[0-9]*|Cm[0-9]*|Bk[0-9]*|Cf[0-9]*|Es[0-9]*|Fm[0-9]*|Md[0-9]*|No[0-9]*|Lr[0-9]*|Ubu[0-9]*|Ubb[0-9]*|Ubt[0-9]*|Ubq[0-9]*|Ubp[0-9]*|Ubh[0-9]*|\\(|\\[|\\)[0-9]*|\\][0-9]*|\\{|\\}[0-9]*)');

    let splittedFormula = formula.split(re);
    splittedFormula.forEach((item, index) => {
      if(item !== ''){
        console.log(multiplier_1 + "          "  + multiplier_2);

        if (item[0] !== '[' && item[0] !== '(' && item[0] !== ')' && item[0] !== ']' && item[0] !== '}' && item[0] !== '{') {
          let temp = item.split(new RegExp(/([0-9]+)/, 'g'));
          if(item.length > 1 && temp[1]) {
            if(atomsAmount[temp[0]]) {
              atomsAmount[temp[0]] += parseInt(temp[1]) * multiplier_1 * multiplier_2 * multiplier_3;
            } else {
              atomsAmount[temp[0]] = parseInt(temp[1]) * multiplier_1 * multiplier_2 * multiplier_3;
            }
          } else {
            if(atomsAmount[item]) {
              atomsAmount[item] += 1 * multiplier_1 * multiplier_2 * multiplier_3;
            } else {
              atomsAmount[item] = 1 * multiplier_1 * multiplier_2 * multiplier_3;
            }
          }
        } else if (item[0] == '[') {
          for(let i = index + 1; i < splittedFormula.length; i++) {
            if(splittedFormula[i][0] === ']') {
              multiplier_1_1 = parseInt(splittedFormula[i].match(/[0-9]+/));
              if (multiplier_1_1) {
                multiplier_1 = multiplier_1_1;
              }
              break;
            }
          }
        } else if(item[0] == '(') {
          for(let i = index + 1; i < splittedFormula.length; i++) {
            if(splittedFormula[i][0] === ')') {
              multiplier_2_1 = parseInt(splittedFormula[i].match(/[0-9]+/));
              if (multiplier_2_1) {
                multiplier_2 = multiplier_2_1;
              }
              break;
            }
          }
        } else if(item[0] == '{') {
          for(let i = index + 1; i < splittedFormula.length; i++) {
            if(splittedFormula[i][0] === '}') {
              multiplier_3_1 = parseInt(splittedFormula[i].match(/[0-9]+/));
              if (multiplier_3_1) {
                multiplier_3 = multiplier_3_1;
              }
              break;
            }
          }
        } else if(item[0] == ']') {
          multiplier_1 = 1;
        } else if(item[0] == ')') {
          multiplier_2 = 1;
        } else if(item[0] == '}') {
          multiplier_3 = 1;
        }
      }
    });
  consoleLog2(atomsAmount);

    return atomsAmount;
  }


  function consoleLog(array) {
    for (let item of array) {
      console.log(item + '\n');
    }
  }

  function consoleLog2(Obj) {
    for (let property in Obj) {
      console.log(property + ":    " + Obj[property]);
    }
    console.log('\n');
  }


  parseMolecule('K4[ON(SO3)2]2');

