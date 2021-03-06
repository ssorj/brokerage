/*
 *
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 *
 */

"use strict";

const $ = document.querySelector.bind(document);
const $$ = document.querySelectorAll.bind(document);

Element.prototype.$ = function () {
  return this.querySelector.apply(this, arguments);
};

Element.prototype.$$ = function () {
  return this.querySelectorAll.apply(this, arguments);
};

window.addEventListener("load", () => {
    let pathNav = $("#-path-nav > div > nav");

    if (pathNav.$$("a").length < 2) {
        $("#-path-nav").style.display = "none";
    }
});

for (let tabs of $$(".tabs")) {
    for (let link of tabs.$$(":scope > nav > a")) {
        link.addEventListener("click", (event) => {
            event.preventDefault();

            let selectedId = new URL(link.href).hash.substr(1)

            for (let ilink of tabs.$$(":scope > nav > a")) {
                if (ilink.href == link.href) {
                    ilink.classList.add("selected");
                } else {
                    ilink.classList.remove("selected");
                }
            }

            for (let pane of tabs.$$(":scope > div")) {
                if (pane.id == selectedId) {
                    pane.style.display = "inherit";
                } else {
                    pane.style.display = "none";
                }
            }
        });
    }

    tabs.$(":scope > nav > a").classList.add("selected");
    tabs.$(":scope > div").style.display = "inherit";
}
