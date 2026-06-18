// // const TYPES=['str','str','num','str','str','str','str'];
// // let rows=RAW.slice(),sortCol=-1,sortDir='none',page=1,perPage=10,q='';
// // function badge(v){return v==='N'?'<span class="pill-i">&#9888; Issues Found</span>':'<span class="pill-c">&#10003; Clean</span>';}
// // function renderBody(){const s=(page-1)*perPage;document.getElementById('tbody').innerHTML=rows.slice(s,s+perPage).map(r=>'<tr><td>'+r[0]+'</td><td>'+r[1]+'</td><td style="text-align:right;font-family:Inter,sans-serif;color:var(--accent);font-weight:600">'+parseInt(r[2]).toLocaleString()+'</td><td>'+badge(r[3])+'</td><td>'+r[4]+'</td><td>'+r[5]+'</td><td>'+r[6]+'</td></tr>').join('');}
// // function renderInfo(){const tot=rows.length,s=Math.min((page-1)*perPage+1,tot),e=Math.min(page*perPage,tot);const note=q?' (filtered from '+RAW.length.toLocaleString()+' total)':'';document.getElementById('pgInfo').textContent=tot===0?'No matching records':'Showing '+s.toLocaleString()+' to '+e.toLocaleString()+' of '+tot.toLocaleString()+' entries'+note;}
// // function renderPg(){const tot=Math.max(1,Math.ceil(rows.length/perPage));let h='';h+='<span class="pgb'+(page===1?' dis':'')+(page===1?' dis':'')+'" onclick="goPage(1)">&#171;</span>';h+='<span class="pgb'+(page===1?' dis':'')+'\" onclick="goPage('+(page-1)+')">&#8249;</span>';let ps=[];if(tot<=7){for(let i=1;i<=tot;i++)ps.push(i);}else{ps=[1];if(page>3)ps.push('...');for(let i=Math.max(2,page-1);i<=Math.min(tot-1,page+1);i++)ps.push(i);if(page<tot-2)ps.push('...');ps.push(tot);}ps.forEach(p=>{if(p==='...')h+='<span class="pgb dis">&#8230;</span>';else h+='<span class="pgb'+(p===page?' act':'')+'" onclick="goPage('+p+')">'+p+'</span>';});h+='<span class="pgb'+(page===tot?' dis':'')+'\" onclick="goPage('+(page+1)+')">&#8250;</span>';h+='<span class="pgb'+(page===tot?' dis':'')+'\" onclick="goPage('+tot+')">&#187;</span>';document.getElementById('pgBtns').innerHTML=h;}
// // function render(){renderBody();renderInfo();renderPg();}
// // function sortTable(col,dir){sortCol=col;sortDir=dir;for(let i=0;i<7;i++){const a=document.querySelector('.sort-asc-'+i),d=document.querySelector('.sort-desc-'+i),n=document.querySelector('.sort-none-'+i);if(a)a.textContent=(col===i&&dir==='asc')?'✓':' ';if(d)d.textContent=(col===i&&dir==='desc')?'✓':' ';if(n)n.textContent=(col===i&&dir==='none')?'✓':' ';}document.querySelectorAll('.th-label').forEach(el=>{const c=parseInt(el.dataset.col);const base=el.dataset.base||(el.dataset.base=el.textContent.trim());el.textContent=base+(c===col?(dir==='asc'?' ↑':dir==='desc'?' ↓':''):'');});document.querySelectorAll('.dots-wrap').forEach(w=>w.blur());if(dir==='none'){rebuildRows();return;}rows.sort((a,b)=>{let av=a[col],bv=b[col];if(TYPES[col]==='num'){av=Number(av);bv=Number(bv);}else{av=String(av).toLowerCase();bv=String(bv).toLowerCase();}return av<bv?(dir==='asc'?-1:1):av>bv?(dir==='asc'?1:-1):0;});page=1;render();}
// //   const wrap=e.target.closest('.dots-wrap');
// //   if(wrap)positionMenu(wrap);
// // });

// // render();







// // const TYPES=['str','str','num','str','str','str','str'];
// // let rows=RAW.slice(),sortCol=-1,sortDir='none',page=1,perPage=10,q='';
// // function badge(v){return v==='N'?'<span class="pill-i">&#9888; Issues Found</span>':'<span class="pill-c">&#10003; Clean</span>';}
// // function renderBody(){const s=(page-1)*perPage;document.getElementById('tbody').innerHTML=rows.slice(s,s+perPage).map(r=>'<tr><td>'+r[0]+'</td><td>'+r[1]+'</td><td style="text-align:right;font-family:Syne,sans-serif;color:var(--accent);font-weight:600">'+parseInt(r[2]).toLocaleString()+'</td><td>'+badge(r[3])+'</td><td>'+r[4]+'</td><td>'+r[5]+'</td><td>'+r[6]+'</td></tr>').join('');}
// // function renderInfo(){const tot=rows.length,s=Math.min((page-1)*perPage+1,tot),e=Math.min(page*perPage,tot);const note=q?' (filtered from '+RAW.length.toLocaleString()+' total)':'';document.getElementById('pgInfo').textContent=tot===0?'No matching records':'Showing '+s.toLocaleString()+' to '+e.toLocaleString()+' of '+tot.toLocaleString()+' entries'+note;}
// // function renderPg(){const tot=Math.max(1,Math.ceil(rows.length/perPage));let h='';h+='<span class="pgb'+(page===1?' dis':'')+'" onclick="goPage(1)">&#171;</span>';h+='<span class="pgb'+(page===1?' dis':'')+'" onclick="goPage('+(page-1)+')">&#8249;</span>';let ps=[];if(tot<=7){for(let i=1;i<=tot;i++)ps.push(i);}else{ps=[1];if(page>3)ps.push('...');for(let i=Math.max(2,page-1);i<=Math.min(tot-1,page+1);i++)ps.push(i);if(page<tot-2)ps.push('...');ps.push(tot);}ps.forEach(p=>{if(p==='...')h+='<span class="pgb dis">&#8230;</span>';else h+='<span class="pgb'+(p===page?' act':'')+'" onclick="goPage('+p+')">'+p+'</span>';});h+='<span class="pgb'+(page===tot?' dis':'')+'" onclick="goPage('+(page+1)+')">&#8250;</span>';h+='<span class="pgb'+(page===tot?' dis':'')+'" onclick="goPage('+tot+')">&#187;</span>';document.getElementById('pgBtns').innerHTML=h;}
// // function render(){renderBody();renderInfo();renderPg();}
// // function sortTable(col,dir){sortCol=col;sortDir=dir;for(let i=0;i<7;i++){const a=document.querySelector('.sort-asc-'+i),d=document.querySelector('.sort-desc-'+i),n=document.querySelector('.sort-none-'+i);if(a)a.textContent=(col===i&&dir==='asc')?'✓':' ';if(d)d.textContent=(col===i&&dir==='desc')?'✓':' ';if(n)n.textContent=(col===i&&dir==='none')?'✓':' ';}document.querySelectorAll('.th-label').forEach(el=>{const c=parseInt(el.dataset.col);const base=el.dataset.base||(el.dataset.base=el.textContent.trim());el.textContent=base+(c===col?(dir==='asc'?' ↑':dir==='desc'?' ↓':''):'');});document.querySelectorAll('.dots-wrap').forEach(w=>w.blur());if(dir==='none'){rebuildRows();return;}rows.sort((a,b)=>{let av=a[col],bv=b[col];if(TYPES[col]==='num'){av=Number(av);bv=Number(bv);}else{av=String(av).toLowerCase();bv=String(bv).toLowerCase();}return av<bv?(dir==='asc'?-1:1):av>bv?(dir==='asc'?1:-1):0;});page=1;render();}
// // function rebuildRows(){rows=q?RAW.filter(r=>r.some(c=>String(c).toLowerCase().includes(q))):RAW.slice();if(sortCol>=0&&sortDir!=='none')rows.sort((a,b)=>{let av=a[sortCol],bv=b[sortCol];if(TYPES[sortCol]==='num'){av=Number(av);bv=Number(bv);}else{av=String(av).toLowerCase();bv=String(bv).toLowerCase();}return av<bv?(sortDir==='asc'?-1:1):av>bv?(sortDir==='asc'?1:-1):0;});page=1;render();}
// // function doSearch(v){q=v.toLowerCase();rebuildRows();}
// // function changePerPage(v){perPage=parseInt(v);page=1;render();}
// // function goPage(p){const t=Math.ceil(rows.length/perPage);if(p<1||p>t)return;page=p;render();}
// // render();







// const TYPES=['str','str','num','str','str','str','str'];
// let rows=RAW.slice(),sortCol=-1,sortDir='none',page=1,perPage=10,q='';
// function badge(v){return v==='N'?'<span class="pill-i">&#9888; Issues Found</span>':'<span class="pill-c">&#10003; Clean</span>';}
// function renderBody(){const s=(page-1)*perPage;document.getElementById('tbody').innerHTML=rows.slice(s,s+perPage).map(r=>'<tr><td>'+r[0]+'</td><td>'+r[1]+'</td><td style="text-align:right;font-family:Syne,sans-serif;color:var(--accent);font-weight:600">'+parseInt(r[2]).toLocaleString()+'</td><td>'+badge(r[3])+'</td><td>'+r[4]+'</td><td>'+r[5]+'</td><td>'+r[6]+'</td></tr>').join('');}
// function renderInfo(){const tot=rows.length,s=Math.min((page-1)*perPage+1,tot),e=Math.min(page*perPage,tot);const note=q?' (filtered from '+RAW.length.toLocaleString()+' total)':'';document.getElementById('pgInfo').textContent=tot===0?'No matching records':'Showing '+s.toLocaleString()+' to '+e.toLocaleString()+' of '+tot.toLocaleString()+' entries'+note;}
// function renderPg(){const tot=Math.max(1,Math.ceil(rows.length/perPage));let h='';h+='<span class="pgb'+(page===1?' dis':'')+(page===1?' dis':'')+'" onclick="goPage(1)">&#171;</span>';h+='<span class="pgb'+(page===1?' dis':'')+'\" onclick="goPage('+(page-1)+')">&#8249;</span>';let ps=[];if(tot<=7){for(let i=1;i<=tot;i++)ps.push(i);}else{ps=[1];if(page>3)ps.push('...');for(let i=Math.max(2,page-1);i<=Math.min(tot-1,page+1);i++)ps.push(i);if(page<tot-2)ps.push('...');ps.push(tot);}ps.forEach(p=>{if(p==='...')h+='<span class="pgb dis">&#8230;</span>';else h+='<span class="pgb'+(p===page?' act':'')+'" onclick="goPage('+p+')">'+p+'</span>';});h+='<span class="pgb'+(page===tot?' dis':'')+'\" onclick="goPage('+(page+1)+')">&#8250;</span>';h+='<span class="pgb'+(page===tot?' dis':'')+'\" onclick="goPage('+tot+')">&#187;</span>';document.getElementById('pgBtns').innerHTML=h;}
// function render(){renderBody();renderInfo();renderPg();}
// function sortTable(col,dir){sortCol=col;sortDir=dir;for(let i=0;i<7;i++){const a=document.querySelector('.sort-asc-'+i),d=document.querySelector('.sort-desc-'+i),n=document.querySelector('.sort-none-'+i);if(a)a.textContent=(col===i&&dir==='asc')?'✓':' ';if(d)d.textContent=(col===i&&dir==='desc')?'✓':' ';if(n)n.textContent=(col===i&&dir==='none')?'✓':' ';}document.querySelectorAll('.th-label').forEach(el=>{const c=parseInt(el.dataset.col);const base=el.dataset.base||(el.dataset.base=el.textContent.trim());el.textContent=base+(c===col?(dir==='asc'?' ↑':dir==='desc'?' ↓':''):'');});document.querySelectorAll('.dots-wrap').forEach(w=>w.blur());if(dir==='none'){rebuildRows();return;}rows.sort((a,b)=>{let av=a[col],bv=b[col];if(TYPES[col]==='num'){av=Number(av);bv=Number(bv);}else{av=String(av).toLowerCase();bv=String(bv).toLowerCase();}return av<bv?(dir==='asc'?-1:1):av>bv?(dir==='asc'?1:-1):0;});page=1;render();}
// function rebuildRows(){rows=q?RAW.filter(r=>r.some(c=>String(c).toLowerCase().includes(q))):RAW.slice();if(sortCol>=0&&sortDir!=='none')rows.sort((a,b)=>{let av=a[sortCol],bv=b[sortCol];if(TYPES[sortCol]==='num'){av=Number(av);bv=Number(bv);}else{av=String(av).toLowerCase();bv=String(bv).toLowerCase();}return av<bv?(sortDir==='asc'?-1:1):av>bv?(sortDir==='asc'?1:-1):0;});page=1;render();}
// function doSearch(v){q=v.toLowerCase();rebuildRows();}
// function changePerPage(v){perPage=parseInt(v);page=1;render();}
// function goPage(p){const t=Math.ceil(rows.length/perPage);if(p<1||p>t)return;page=p;render();}

// /* Position fixed dots-menu relative to its trigger button */
// function positionMenu(wrap){
//   const menu=wrap.querySelector('.dots-menu');
//   if(!menu)return;
//   const btn=wrap.querySelector('.dots-btn');
//   if(!btn)return;
//   const r=btn.getBoundingClientRect();
//   const mw=180;
//   let left=r.right-mw;
//   if(left<4)left=4;
//   let top=r.bottom+4;
//   const vh=window.innerHeight;
//   const mh=120; // approximate menu height
//   if(top+mh>vh)top=r.top-mh-4;
//   menu.style.top=top+'px';
//   menu.style.left=left+'px';
//   menu.style.minWidth=mw+'px';
// }

// document.addEventListener('focusin',function(e){
//   const wrap=e.target.closest('.dots-wrap');
//   if(wrap)positionMenu(wrap);
// });

// render();










const TYPES=['str','str','num','str','str','str','str'];
let rows=RAW.slice(),sortCol=-1,sortDir='none',page=1,perPage=10,q='';
function badge(v){return v==='N'?'<span class="pill-i">&#9888; Issues Found</span>':'<span class="pill-c">&#10003; Clean</span>';}
function renderBody(){const s=(page-1)*perPage;document.getElementById('tbody').innerHTML=rows.slice(s,s+perPage).map(r=>'<tr><td>'+r[0]+'</td><td>'+r[1]+'</td><td style="text-align:right;font-family:Syne,sans-serif;color:var(--accent);font-weight:600">'+parseInt(r[2]).toLocaleString()+'</td><td>'+badge(r[3])+'</td><td>'+r[4]+'</td><td>'+r[5]+'</td><td>'+r[6]+'</td></tr>').join('');}
function renderInfo(){const tot=rows.length,s=Math.min((page-1)*perPage+1,tot),e=Math.min(page*perPage,tot);const note=q?' (filtered from '+RAW.length.toLocaleString()+' total)':'';document.getElementById('pgInfo').textContent=tot===0?'No matching records':'Showing '+s.toLocaleString()+' to '+e.toLocaleString()+' of '+tot.toLocaleString()+' entries'+note;}
function renderPg(){const tot=Math.max(1,Math.ceil(rows.length/perPage));let h='';h+='<span class="pgb'+(page===1?' dis':'')+'" onclick="goPage(1)">&#171;</span>';h+='<span class="pgb'+(page===1?' dis':'')+'" onclick="goPage('+(page-1)+')">&#8249;</span>';let ps=[];if(tot<=7){for(let i=1;i<=tot;i++)ps.push(i);}else{ps=[1];if(page>3)ps.push('...');for(let i=Math.max(2,page-1);i<=Math.min(tot-1,page+1);i++)ps.push(i);if(page<tot-2)ps.push('...');ps.push(tot);}ps.forEach(p=>{if(p==='...')h+='<span class="pgb dis">&#8230;</span>';else h+='<span class="pgb'+(p===page?' act':'')+'" onclick="goPage('+p+')">'+p+'</span>';});h+='<span class="pgb'+(page===tot?' dis':'')+'" onclick="goPage('+(page+1)+')">&#8250;</span>';h+='<span class="pgb'+(page===tot?' dis':'')+'" onclick="goPage('+tot+')">&#187;</span>';document.getElementById('pgBtns').innerHTML=h;}
function render(){renderBody();renderInfo();renderPg();}
function sortTable(col,dir){sortCol=col;sortDir=dir;for(let i=0;i<7;i++){const a=document.querySelector('.sort-asc-'+i),d=document.querySelector('.sort-desc-'+i),n=document.querySelector('.sort-none-'+i);if(a)a.textContent=(col===i&&dir==='asc')?'✓':' ';if(d)d.textContent=(col===i&&dir==='desc')?'✓':' ';if(n)n.textContent=(col===i&&dir==='none')?'✓':' ';}document.querySelectorAll('.th-label').forEach(el=>{const c=parseInt(el.dataset.col);const base=el.dataset.base||(el.dataset.base=el.textContent.trim());el.textContent=base+(c===col?(dir==='asc'?' ↑':dir==='desc'?' ↓':''):'');});document.querySelectorAll('.dots-wrap').forEach(w=>w.blur());if(dir==='none'){rebuildRows();return;}rows.sort((a,b)=>{let av=a[col],bv=b[col];if(TYPES[col]==='num'){av=Number(av);bv=Number(bv);}else{av=String(av).toLowerCase();bv=String(bv).toLowerCase();}return av<bv?(dir==='asc'?-1:1):av>bv?(dir==='asc'?1:-1):0;});page=1;render();}
function rebuildRows(){rows=q?RAW.filter(r=>r.some(c=>String(c).toLowerCase().includes(q))):RAW.slice();if(sortCol>=0&&sortDir!=='none')rows.sort((a,b)=>{let av=a[sortCol],bv=b[sortCol];if(TYPES[sortCol]==='num'){av=Number(av);bv=Number(bv);}else{av=String(av).toLowerCase();bv=String(bv).toLowerCase();}return av<bv?(sortDir==='asc'?-1:1):av>bv?(sortDir==='asc'?1:-1):0;});page=1;render();}
function doSearch(v){q=v.toLowerCase();rebuildRows();}
function changePerPage(v){perPage=parseInt(v);page=1;render();}
function goPage(p){const t=Math.ceil(rows.length/perPage);if(p<1||p>t)return;page=p;render();}
render();
