---
date: '2025-05-28'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a7ab2bd...MicrosoftDocs:4f76879
summary: この変更では、ドキュメント内の誤った役割名「Contributer」が「Contributor」に修正されました。これにより、Azureにおける役割名の正確性が向上し、Azure
  Search Serviceの設定手順での混乱を防ぐことが目的です。新機能の追加はありませんが、手順の正確性が向上し、この修正は非破壊的でユーザーへの影響はありません。また、手順1と手順2で役割名の位置や誤ったスペルも修正されました。正確な役割名の使用は、ユーザーが適切な権限設定を行う上で重要であり、このような修正がユーザーエクスペリエンスを向上させます。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a7ab2bd...MicrosoftDocs:4f76879){target="_blank"}

# ハイライト
この変更では、ドキュメント内の「*Contributer*」という誤った役割名が「*Contributor*」に修正されました。これは、Azureの役割名を正確にし、Azure Search Service に関連する設定手順における混乱を防ぐことを目的としています。

## 新機能
特に新機能は追加されていませんが、設定手順の正確性が向上しました。

## 破壊的変更
この修正は非破壊的変更であり、ユーザーへの影響はありません。

## その他の更新
手順1と手順2の両方で役割名の位置が更新され、誤ったスペルが使用されていた箇所が修正されました。

# インサイト
Azureのドキュメントにおいて、正確な役割名を使用することは非常に重要です。誤った役割名が使用されていると、ユーザーが適切な権限設定を行えず、サービスの利用に支障をきたす可能性があります。特に「Contributor」という役割は、リソースへのアクセス権を決定する上で重要な要素となるため、この種の修正はユーザーエクスペリエンスを向上させます。適切な役割名が明記されていることで、ユーザーはより簡単に正しい設定を適用することができ、結果としてAzure Search Serviceの導入や利用がスムーズになります。このような小さな修正は、一見すると目立たないかもしれませんが、ユーザーに与える影響は大きく、ドキュメントの信頼性を高めるために必要不可欠です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [network-isolation.md](#item-8445fc) | minor update | 役割名の修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/language-service/question-answering/how-to/network-isolation.md{#item-8445fc}

<details>
<summary>Diff</summary>
````diff
@@ -21,12 +21,12 @@ Private endpoints are provided by [Azure Private Link](/azure/private-link/priva
 
 ## Steps to enable private endpoint
 
-1. Assign *Contributer* role to language resource (Depending on the context this may appear as a Text Analytics resource) in the Azure Search Service instance. This operation requires *Owner* access to the subscription. Go to Identity tab in the service resource to get the identity.
+1. Assign *Contributor* role to language resource (Depending on the context this may appear as a Text Analytics resource) in the Azure Search Service instance. This operation requires *Owner* access to the subscription. Go to Identity tab in the service resource to get the identity.
 
 > [!div class="mx-imgBorder"]
 > ![Text Analytics Identity](../../../QnAMaker/media/qnamaker-reference-private-endpoints/private-endpoints-identity.png)
 
-2. Add the above identity as *Contributer* by going to Azure Search Service IAM tab.
+2. Add the above identity as *Contributor* by going to Azure Search Service IAM tab.
 
 ![Managed service IAM](../../../QnAMaker/media/qnamaker-reference-private-endpoints/private-endpoint-access-control.png)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "役割名の修正"
}
```

### Explanation
この変更では、ドキュメント内の「*Contributer*」という役割名が「*Contributor*」に修正されています。この変更は、Azureの役割名に正確さを持たせるためのものであり、特にAzure Search Serviceに関連する設定手順において混乱を防ぐことが目的です。具体的には、手順1と手順2の両方でこの役割名の位置が更新されています。変更前の文書では誤ったスペルが使用されていましたが、修正後は正確な役割名を使用することで、ユーザーが適切な権限を割り当てることができるようになります。この修正により、ドキュメントの正確性とユーザー体験が向上します。


