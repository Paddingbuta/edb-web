<template>
    <div class="contents">
        <!-- <router-link to="/cybersploit">CyberSploit: Large Scale Proof-of-Concept Databse</router-link>
        <br>
        <a href="http://harmonyflow.sctruster.com:8080/">harmonyflow</a>
        <br>
        <a href="http://159.75.80.253:8888/mutisource">mutisource</a> -->

        <div class="card">
            <div>
                <div class="number">01</div>
                <div class="text">
                    <span>CyberSploit</span>
                </div>
                <router-link to="/cybersploit">
                    <button class="contactButton">
                        Entry
                        <div class="iconButton">
                            <svg height="24" width="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0 0h24v24H0z" fill="none"></path>
                                <path
                                    d="M16.172 11l-5.364-5.364 1.414-1.414L20 12l-7.778 7.778-1.414-1.414L16.172 13H4v-2z"
                                    fill="currentColor"></path>
                            </svg>
                        </div>
                    </button>
                </router-link>
            </div>
        </div>
        <div class="card">
            <div>
                <div class="number">02</div>
                <div class="text">
                    <span>Harmonyflow</span>
                </div>
                <a href="http://harmonyflow.sctruster.com:8080/">
                    <button class="contactButton">
                        Entry
                        <div class="iconButton">
                            <svg height="24" width="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0 0h24v24H0z" fill="none"></path>
                                <path
                                    d="M16.172 11l-5.364-5.364 1.414-1.414L20 12l-7.778 7.778-1.414-1.414L16.172 13H4v-2z"
                                    fill="currentColor"></path>
                            </svg>
                        </div>
                    </button>
                </a>
            </div>
        </div>
        <div class="card">
            <div>
                <div class="number">03</div>
                <div class="text">
                    <span>Mutisource</span>
                </div>
                <a href="http://159.75.80.253:8888/mutisource">
                    <button class="contactButton">
                        Entry
                        <div class="iconButton">
                            <svg height="24" width="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0 0h24v24H0z" fill="none"></path>
                                <path
                                    d="M16.172 11l-5.364-5.364 1.414-1.414L20 12l-7.778 7.778-1.414-1.414L16.172 13H4v-2z"
                                    fill="currentColor"></path>
                            </svg>
                        </div>
                    </button>
                </a>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Root'
}
</script>

<style scoped>
.contents {
    width: 100%;
    margin-top: 60px;
    margin-bottom: 60px;
    display: flex;
    justify-content: center;
    gap: 100px;
    padding: 20px;
}

.card {
    position: relative;
    box-sizing: border-box;
    width: 300px;
    height: 400px;
    /* background: rgba(99, 187, 228, 0.103); */
    /* border: 1px solid white; */
    box-shadow: 12px 17px 51px rgba(3, 50, 219, 0.22);
    backdrop-filter: blur(6px);
    border-radius: 50px;
    text-align: center;
    cursor: pointer;
    transition: all 0.5s;
    display: flex;
    align-items: center;
    justify-content: center;
    user-select: none;
    font-weight: bolder;
    color: black;
}

.number {
    position: absolute;
    top: 50px;
    left: 130px;
    width: 30px;
    height: 30px;
    font-size: 40px;
    text-transform: uppercase;
    padding: 0px 5px 0px 8px;
    color: #9b9ced;
    background: rgba(228, 142, 99, 0.103);
}

.text {
    flex-grow: 1;
    padding: 15px;
    display: flex;
    flex-direction: column;
    color: rgb(117, 139, 237);
    font-weight: 900;
    font-size: 1.2em;
}

.contactButton {
    position: absolute;
    top: 330px;
    left: 100px;
    background: #adb1ef;
    color: white;
    font-family: inherit;
    padding: 0.45em;
    padding-left: 1em;
    font-size: 17px;
    font-weight: 500;
    border-radius: 0.9em;
    border: none;
    cursor: pointer;
    letter-spacing: 0.05em;
    display: flex;
    align-items: center;
    box-shadow: inset 0 0 1.6em -0.6em #714da6;
    overflow: hidden;
    height: 2.8em;
    padding-right: 3em;
}

.iconButton {
    margin-left: 1em;
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 2.2em;
    width: 2.2em;
    border-radius: 0.7em;
    box-shadow: 0.1em 0.1em 0.6em 0.2em #7a8cf3;
    right: 0.3em;
    transition: all 0.3s;
}

.contactButton:hover {
    transform: translate(-0.05em, -0.05em);
    box-shadow: 0.15em 0.15em #5566c2;
}

.contactButton:active {
    transform: translate(0.05em, 0.05em);
    box-shadow: 0.05em 0.05em #5566c2;
}
</style>