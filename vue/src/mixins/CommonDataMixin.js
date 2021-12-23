/* eslint-disable no-unused-vars */
function format (v) {
  const reg = /\d{1,3}(?=(\d{3})+$)/g
  return `${v}`.replace(reg, '$&,')
}

function wrapperObject (o, k) {
  if (o && k.indexOf('.') >= 0) {
    const keys = k.split('.')
    keys.forEach(key => {
      o = o[key]
    })
    return o
  } else {
    return o && o[k] ? o[k] : {}
  }
}

function wrapperArray (o, k) {
  return o && o[k] ? o[k] : [200, 233, 221, 323, 122, 212, 200, 233, 221, 323, 122, 212]
}

function wrapperMoney (o, k) {
  return o && o[k] ? `¥ ${format(o[k])}` : '¥ 0.00'
}

function wrapperOriginalNumber (o, k) {
  return o && o[k] ? o[k] : 0
}

function wrapperNumber (o, k) {
  return o && o[k] ? format(o[k]) : 0
}

function wrapperPercentage (o, k) {
  return o && o[k] ? `${o[k]}%` : '0%'
}

export default {
    computed: {
      reportdata () {
        return this.getReportData()
      },
      month () {
        // console.log(this.reportdata)
        return this.reportdata ? this.reportdata.time.month : [200, 233, 221, 323, 122, 212, 200, 233, 221, 323, 122, 212]
      },
      quarter () {
        return this.reportdata ? this.reportdata.time.quarter : [21, 31, 21, 23]
      },
      shop () {
        return this.reportdata ? this.reportdata.shop : []
      },
      two () {
        return this.reportdata ? this.reportdata.two : []
      },
      category1 () {
        return this.reportdata ? this.reportdata.category : []
      }
    },
    inject: ['getReportData']
}
