<template>
    <div class="home-container">
        <div class="home-content">
            <div class="block">
                <el-carousel class="lun_imgs" ref="carousel" interval="4000" type="card" height="470px" >
                    <el-carousel-item v-for="item in dataimg" v-bind:key="item.url" >
                    <img :src="item.url" style="width:100%"/>
                    </el-carousel-item>
                </el-carousel>
            </div>
            <div style="float:right">
            <h3>项目地址</h3>
            <a target="_blank" href="https://github.com/How-young/hotelManagementSystem">
            <el-image :src="src" style="width: 100px; height: 100px"></el-image>
            </a>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'home',
    data() {
        return {
            dataimg: [
                { url: require('../assets/imgs/img1.jpg') },
                { url: require('../assets/imgs/img2.jpg') },
                { url: require('../assets/imgs/img3.jpg') },
                { url: require('../assets/imgs/img4.jpg') },
                { url: require('../assets/imgs/img5.jpg') },
            ],
            src: 'https://dss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2902802496,2294820017&fm=26&gp=0.jpg',
        }
    },
    methods: {
    },
}
</script>

<style scoped>
    .home-container {
        padding: 10px;
        padding-top: 5px;
    }
    .home-content {
        padding: 10px;
        border-radius: 5px;
        background: #fff;
    }
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>
